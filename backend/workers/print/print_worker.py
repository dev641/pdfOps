# backend/worker.py
from PySide6.QtCore import QObject, Signal
from backend.services.print.print_service import (
    PrintService,
    PrinterSettingsDTO,
    PrintResult,
)
from common.enums.enums import JobStatus


class PrintWorker(QObject):
    progress = Signal(str, int, str)  # path, JobStatus.value, message
    finished = Signal()

    def __init__(
        self,
        file_list: list[str],
        settings: PrinterSettingsDTO,
        service: PrintService,
    ):
        super().__init__()
        self.file_list = file_list
        self.settings = settings
        self.service = service
        self._should_stop = False

    def run(self):
        for p in self.file_list:
            if self._should_stop:
                break
            self.progress.emit(p, JobStatus.IN_PROGRESS.value, "Printing...")
            try:
                res: PrintResult = self.service.print_one(p, self.settings)
                if res.ok:
                    self.progress.emit(p, JobStatus.DONE.value, "Printed")
                else:
                    self.progress.emit(
                        p, JobStatus.ERROR.value, res.stderr or "Error"
                    )
            except Exception as e:
                self.progress.emit(p, JobStatus.ERROR.value, str(e))
        self.finished.emit()

    def stop(self):
        self._should_stop = True
