from PySide6.QtCore import QThread
from backend.services.flattenFolder.flatten_folder_service import (
    FlattenFolderService,
)


class FlattenFolderWorker(QThread):
    """
    Runs the FlattenFolderService in a separate thread.
    Exposes the same signals for UI connection.
    """

    def __init__(self, src_folder: str, dest_folder: str, parent=None):
        super().__init__(parent)
        self.src_folder = src_folder
        self.dest_folder = dest_folder
        self.service = FlattenFolderService()
        self.service.moveToThread(self)

        # Pass through signals
        self.progressChanged = self.service.progressChanged
        self.finishedProcessing = self.service.finishedProcessing

    def run(self):
        self.service.copy_all(self.src_folder, self.dest_folder)

    def stop(self):
        self.service.stop()
