from pathlib import Path
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox
from frontend.components.ProgressDialog.progress_dialog import ProgressDialog
from backend.workers.flatten_folder_worker import FlattenFolderWorker


class FlattenFolderController(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self._worker = None
        self._progress = None

    def on_folders_selected(self, src_folder: str, dest_folder: str):
        total = len(list(Path(src_folder).rglob("*.pdf")))
        if total == 0:
            QMessageBox.information(
                self.parent,
                "No PDFs Found",
                "No PDF files were found in the selected source folder.",
            )
            return

        self._progress = ProgressDialog(total_files=total, parent=self.parent)

        self._worker = FlattenFolderWorker(
            src_folder, dest_folder, parent=self.parent
        )
        self._worker.progressChanged.connect(self._on_progress_changed)
        self._worker.finishedProcessing.connect(self._on_finished)

        self._progress.cancel_button.clicked.connect(self._worker.stop)

        self._worker.start()
        self._progress.exec()

    def _on_progress_changed(self, processed: int, total: int, filename: str):
        if self._progress:
            self._progress.update_progress(processed, total, filename)

    def _on_finished(self, processed: int, skipped: int, canceled: bool):
        if self._progress and self._progress.isVisible():
            self._progress.accept()

        title = "Flatten Canceled" if canceled else "Flatten Completed"
        QMessageBox.information(
            self.parent, title, f"Processed: {processed}\nSkipped: {skipped}"
        )

        if self._worker:
            self._worker.wait(2000)
        self._worker = None
        self._progress = None
