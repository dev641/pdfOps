from pathlib import Path
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from common.enums.enums import ActionType


class FolderSelector(QWidget):
    foldersSelected = Signal(str, str, ActionType)  # src_folder, dest_folder

    def __init__(self, parent=None):
        super().__init__(parent)

    def chooseSourceAndDestination(self, sourceRequired=True, action=None):
        src_folder = None
        if sourceRequired:
            src_folder = QFileDialog.getExistingDirectory(
                self, "Select Source Folder"
            )
            if not src_folder:
                return
        else:
            # If source not required, emit empty string to indicate that
            src_folder = ""
            print(
                "No source folder required, proceeding with destination selection"
            )

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

        self.foldersSelected.emit(src_folder, dest_folder, action)
