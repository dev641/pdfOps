from .directory_selection import DirectorySelection
from .file_selection import FileSelection
from ..ComboBox.comboBox import ComboBox
from common.enums.enums import UserSelectionType, FileSectionType
from backend.controller.file_handler import FileHandler


class FileDirectorySelection(FileSelection, DirectorySelection):
    def __init__(self):
        super().__init__()
        items = UserSelectionType.get_all_options()
        self.comboBox = ComboBox(
            items=items, parent=self, onItemSelected=self.onItemSelected
        )

    def onItemSelected(self, index):
        """Handle item selection in the combo box."""
        item = self.comboBox.itemText(index)
        if item == UserSelectionType.FILE.value:
            self.selectFiles()
        elif item == UserSelectionType.DIRECTORY.value:
            self.selectDirectories()
        else:
            print("Invalid selection.")
