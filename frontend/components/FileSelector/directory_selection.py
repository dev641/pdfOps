from PySide6.QtWidgets import QFileDialog, QWidget
from backend.controller.file_handler import FileHandler


class DirectorySelection(QWidget, FileHandler):
    def __init__(self):
        super().__init__()

    def selectDirectories(self):
        """Open a dialog to select a directory."""
        directoryDialog = QFileDialog(self, "Select Directory")
        directoryDialog.setFileMode(QFileDialog.Directory)
        directoryDialog.setOption(QFileDialog.ReadOnly, True)

        # Get the selected directory path
        directory = directoryDialog.getExistingDirectory()

        if directory:
            self.handleDirectory(directories=[directory])
            return directory  # Return the selected directory
        else:
            return None  # No directory selected
