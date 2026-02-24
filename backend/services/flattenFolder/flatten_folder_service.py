from pathlib import Path
import shutil
from PySide6.QtCore import QObject, Signal
from ..baseTasks.base_tasks_service import BaseTaskService


class FlattenFolderService(BaseTaskService):

    def __init__(self, src_folder: str, dest_folder: str, parent=None):
        super().__init__(parent)
        self.src_folder = src_folder
        self.dest_folder = dest_folder
        self._is_running = True

    def stop(self):
        self._is_running = False

    def execute(self):
        src = Path(self.src_folder)
        dest = Path(self.dest_folder)
        dest.mkdir(parents=True, exist_ok=True)

        pdfs = list(src.rglob("*.pdf"))
        total = len(pdfs)

        name_counts = {}
        processed, skipped = 0, 0

        for idx, fpath in enumerate(pdfs, start=1):

            if not self._is_running:
                self.finishedProcessing.emit(processed, skipped, True)
                return

            key = fpath.stem.lower()
            if key in name_counts:
                name_counts[key] += 1
                target = (
                    dest / f"{fpath.stem}_{name_counts[key]}{fpath.suffix}"
                )
            else:
                name_counts[key] = 0
                target = dest / f"{fpath.stem}{fpath.suffix}"

            try:
                shutil.copy2(fpath, target)
                processed += 1
            except Exception:
                skipped += 1

            self.progressChanged.emit(idx, total, fpath.name)

        self.finishedProcessing.emit(processed, skipped, False)
