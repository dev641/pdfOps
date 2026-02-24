from concurrent.futures import ProcessPoolExecutor, as_completed
import os
import multiprocessing
from backend.functions.process_pdfs import process_single_pdf
from backend.services.baseTasks.base_tasks_service import BaseTaskService


class PrintFriendlyBatchService(BaseTaskService):

    def __init__(self, pdf_list: list[str], output_dir: str):
        super().__init__()
        self.pdf_list = pdf_list
        self.output_dir = output_dir
        self._is_running = True

    def stop(self):
        self._is_running = False

    def execute(self):

        total = len(self.pdf_list)
        processed = 0
        skipped = 0

        max_workers = max(1, multiprocessing.cpu_count() - 1)

        with ProcessPoolExecutor(max_workers=max_workers) as executor:

            future_map = {}

            for pdf_path in self.pdf_list:

                if not self._is_running:
                    executor.shutdown(cancel_futures=True)
                    self.finishedProcessing.emit(processed, skipped, True)
                    return

                output_path = os.path.join(
                    self.output_dir, os.path.basename(pdf_path)
                )

                future = executor.submit(
                    process_single_pdf, pdf_path, output_path
                )

                future_map[future] = pdf_path

            for future in as_completed(future_map):

                if not self._is_running:
                    executor.shutdown(cancel_futures=True)
                    self.finishedProcessing.emit(processed, skipped, True)
                    return

                try:
                    future.result()
                    processed += 1
                except Exception:
                    skipped += 1

                self.progressChanged.emit(processed, total, "")

        self.finishedProcessing.emit(processed, skipped, False)
