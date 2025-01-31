from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
import os
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from .drag_drop_selection import DragDropSelection
from .file_directory_selection import FileDirectorySelection
from ..Buttons.button import Button
from ..Labels.label import LabeledText
from frontend.container.Layouts.layout_widget import VerticalLayoutWidget
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal
from common.enums.enums import MergeType, Rate


class DragDropFileSelection(
    VerticalLayoutWidget, DragDropSelection, FileDirectorySelection
):

    fileSignal = Signal(list)
    saveFileSignal = Signal(str)
    mergePdfsSignal = Signal(list, str, bool)
    pageRateSignal = Signal(float)

    def __init__(self):
        super().__init__()
        self.label = LabeledText("Drag and drop files or directories here.")
        self.addWidget(self.label)
        self.addWidget(self.comboBox, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #345678;")  # Light Green
        # self.fileSignal.connect(self.emit_fileSignal)
        self.setLayout(self.layout)

    def clearSelection(self):
        """Custom method to clear the selection (files or directories)."""
        print("Selection cleared.")
        self.label.setText("Drag and drop files or directories here.")

    # def emit_fileSignal(self, filePaths):
    #     print("Emitting file signal:", filePaths)

    def onComplete(self):
        super().onComplete()
        self.fileSignal.emit(self.filePaths())
        # self.saveFile

    def saveFile(self):
        file_path = self.getOutputFileFromUser()
        self.saveFileSignal.emit(file_path)

    def mergePdfs(self):
        userSelection = self.getUserSelection(
            title="Select Merge Type",
            dropDownOptions=[
                MergeType.ADD_BLANK_PAGE.value,
                MergeType.DO_NOT_ADD_BLANK_PAGE.value,
            ],
        )
        add_blank_page = userSelection == MergeType.ADD_BLANK_PAGE.value
        outputFile = self.getOutputFileFromUser()
        self.mergePdfsSignal.emit(self.filePaths(), outputFile, add_blank_page)

    def calculate_cost(self):
        userSelection = self.getUserSelection(
            title="Select Rate",
            dropDownOptions=Rate.get_all_options(),
        )
        rate = float(userSelection)
        self.pageRateSignal.emit(rate)


# print(DragDropFileSelection.mro())
