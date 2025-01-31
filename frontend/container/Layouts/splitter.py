from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSplitter
from PySide6.QtCore import Qt


class Splitter(QSplitter):
    def __init__(
        self,
        widget_1=None,
        widget_2=None,
        orientation=Qt.Horizontal,
        handle_width=5,
        stretch_factor=[3, 7],
    ):
        super().__init__(orientation)
        self.widget_1 = widget_1
        self.widget_2 = widget_2
        self._createSplitter(handle_width, stretch_factor)

    def _createSplitter(self, handle_width=5, stretch_factor=[3, 7]):
        self.setHandleWidth(
            handle_width
        )  # Set the width of the splitter handle
        # Add the widgets to the splitter
        self.addWidget(self.widget_1)
        self.addWidget(self.widget_2)

        # Set the initial splitter ratio
        self.setStretchFactor(0, stretch_factor[0])  # 30% for the left section
        self.setStretchFactor(
            1, stretch_factor[1]
        )  # 70% for the right section
