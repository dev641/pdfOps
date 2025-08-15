from pathlib import Path
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox


class FolderSelector(QWidget):
    foldersSelected = Signal(str, str)  # src_folder, dest_folder

    def __init__(self, parent=None):
        super().__init__(parent)

    def chooseSourceAndDestination(self):
        src_folder = QFileDialog.getExistingDirectory(
            self, "Select Source Folder"
        )
        if not src_folder:
            return

        dest_folder = QFileDialog.getExistingDirectory(
            self, "Select Destination Folder"
        )
        if not dest_folder:
            return

        # Warn if destination not empty
        try:
            if any(Path(dest_folder).iterdir()):
                reply = QMessageBox.warning(
                    self,
                    "Destination Not Empty",
                    "The destination folder is not empty. Files might be overwritten.\nContinue?",
                    QMessageBox.Yes | QMessageBox.No,
                )
                if reply == QMessageBox.No:
                    return
        except Exception:
            # If we can't iterate (permissions), still allow continue
            pass

        self.foldersSelected.emit(src_folder, dest_folder)
