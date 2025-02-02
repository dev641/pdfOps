from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt, Signal
from frontend.components.Buttons.button import Button

# from frontend.components.Labels.label import LabeledText
from .layout_widget import VerticalLayoutWidget
from common.enums.enums import PageEnum, ActionType

# from common.utils.debug_layout_structure import debug_layout


class LeftSectionWidget(VerticalLayoutWidget):
    leftSectionNavigationSignal = Signal(ActionType)

    def __init__(self):
        super().__init__()
        self.createLeftSection()
        self.setStyleSheet("background-color: #ADD8E6;")  # Light Blue
        # debug_layout(self)

    def createLeftSection(self):
        # Create the layout for the left section
        self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins

        # self.addWidget(
        #     widget=Button(
        #         "Select Files", onClick=self.emitSelectDirectorySignal
        #     )
        # )
        # self.addWidget(
        #     widget=Button("Go To Table", onClick=self.emitGoToTableSignal)
        # )

        self.addWidget(
            widget=Button("Select Rate", onClick=self.emitSelectRateSignal)
        )
        self.addWidget(
            widget=Button("Create PDF", onClick=self.emitCreatePdfSignal)
        )
        self.addWidget(
            widget=Button("Merge PDF", onClick=self.emitMergePdfsSignal)
        )
        # Add the label to the layout
        # Set the layout for this widget
        self.setLayout(self.layout)

    def addWidget(self, widget: QWidget) -> None:
        super().addWidget(widget)

    def emitSelectDirectorySignal(self):
        self.leftSectionNavigationSignal.emit(ActionType.SELECT_DIRECTORY)

    def emitGoToTableSignal(self):
        self.leftSectionNavigationSignal.emit(ActionType.GO_TO_TABLE)

    def emitCreatePdfSignal(self):
        self.leftSectionNavigationSignal.emit(ActionType.CREATE_PDF)

    def emitSelectRateSignal(self):
        self.leftSectionNavigationSignal.emit(ActionType.SELECT_RATE)

    def emitMergePdfsSignal(self):
        print("Merging PDFs...")
        self.leftSectionNavigationSignal.emit(ActionType.MERGE_PDF)

    def enableButtons(self, enable: bool):
        # for button in self.layout.itemAt(0).widget().children():
        #     button.setEnabled(enable)
        for index in range(self.layout.count()):
            child = self.layout.itemAt(index).widget()
            if isinstance(child, Button):
                child.enableButton(enable=enable)
