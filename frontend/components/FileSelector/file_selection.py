from PySide6.QtWidgets import QFileDialog, QWidget
from backend.controller.file_handler import FileHandler
from common.enums.enums import FileSectionType, AcceptedFileType
from PySide6.QtCore import Signal
from frontend.components.ComboBoxDialog.combo_box_dialog import ComboBoxDialog
from common.enums.enums import MergeType


class FileSelection(QWidget, FileHandler):

    def __init__(self, selectionType=FileSectionType.MULTIPLE_FILES):
        super().__init__()
        self.selectionType = selectionType
        self.fileFilter = (
            f"{AcceptedFileType.PDF.value};;{AcceptedFileType.ALL.value}"
        )

    def selectFiles(self):
        """Open a dialog to select multiple files."""
        fileDialog = QFileDialog(self, "Select File(s)")
        fileDialog.setFileMode(QFileDialog.ExistingFiles)
        fileDialog.setOption(QFileDialog.ReadOnly, True)
        # Get the selected file paths
        filePaths, _ = (
            fileDialog.getOpenFileName(filter=self.fileFilter)
            if self.selectionType == FileSectionType.SINGLE_FILE
            else fileDialog.getOpenFileNames(filter=self.fileFilter)
        )

        if filePaths:
            self.handleFiles(filePaths)
            return filePaths  # Return list of selected files
        else:
            return None  # No files selected

    def getOutputFileFromUser(
        self, fileType: AcceptedFileType = AcceptedFileType.PDF
    ):
        """Save the PDF file."""
        # Open a file dialog to ask for the directory and filename
        fileDialog = QFileDialog(self, "Save PDF", "", filter=self.fileFilter)
        fileDialog.setDefaultSuffix("pdf")  # Default file extension is .pdf
        fileDialog.setAcceptMode(
            QFileDialog.AcceptSave
        )  # Switch to "Save" mode
        fileDialog.setFileMode(
            QFileDialog.AnyFile
        )  # Allow both files and directories, but generally expect file names

        if fileDialog.exec() == QFileDialog.Accepted:
            # Get the file path chosen by the user
            filePath = fileDialog.selectedFiles()[0]
            # Call the method to generate and save the PDF at the chosen path
            # self.create_pdf(filePath)
            print(filePath)
        return filePath

    def getUserSelection(self, title="Select Merge Type", dropDownOptions=[]):

        comboDialog = ComboBoxDialog(
            title=title,
            dropDownOptions=dropDownOptions,
            # on_item_selected=on_item_selected,
        )
        selectedOption = comboDialog.getSelectedOption()
        if selectedOption:
            print(f"User selected: {selectedOption}")
            return selectedOption
        else:
            print("Dialog canceled.")
            return None
