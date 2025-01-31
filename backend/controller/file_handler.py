import os
from PySide6.QtCore import QObject, Signal
from common.utils.utils import is_pdf
from common.models.file_list import FileList


class FileHandler(QObject):
    _filePaths = FileList()
    onComplete = Signal()

    def __init__(self, filePaths: list = None):
        pass

    @classmethod
    def filePaths(cls):
        """Return the filePaths list (read-only access)."""
        return cls._filePaths

    def handleDirectory(self, directories):
        """Handle directories dropped."""
        # print(f"Directory(ies) dropped: {directories}")
        for directory in directories:
            print(f"Contents of {directory}:")
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if is_pdf(file_path):
                        self.filePaths().append(file_path)
                        print(f"Found file: {file_path}")

        self.onComplete()

    def handleFiles(self, files):
        """Handle files dropped."""
        # print(f"Files dropped: {files}")
        for file in files:
            self.filePaths().append(file)
            print(f"Processing file: {file}")
        self.onComplete()

    def onComplete(self):
        print("File handling completed.")
