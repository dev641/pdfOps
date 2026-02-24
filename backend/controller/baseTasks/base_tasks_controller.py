from pathlib import Path
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox
from frontend.components.ProgressDialog.progress_dialog import ProgressDialog
from backend.workers.task_runner import TaskRunner


class BaseTaskController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self._runner = None
        self._progress = None

    def start_service(self, service, total_files, title="Processing"):
        self._progress = ProgressDialog(total_files, parent=self.parent)

        self._runner = TaskRunner(service, parent=self.parent)

        self._runner.progressChanged.connect(self._on_progress)
        self._runner.finishedProcessing.connect(self._on_finish)

        self._progress.cancel_button.clicked.connect(self._runner.stop)

        self._runner.start()
        self._progress.exec()

    def _on_progress(self, processed, total, filename):
        if self._progress:
            self._progress.update_progress(processed, total, filename)

    def _on_finish(self, processed, skipped, canceled):
        if self._progress and self._progress.isVisible():
            self._progress.accept()

        title = "Canceled" if canceled else "Completed"
        QMessageBox.information(
            self.parent,
            title,
            f"Processed: {processed}\nSkipped: {skipped}",
        )

        self._runner = None
        self._progress = None
