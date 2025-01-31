from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class LabeledText(QLabel):
    def __init__(
        self,
        text,
        parent=None,
        font_size=12,
        alignment=Qt.AlignCenter,
        color="black",
    ):
        """
        A reusable label class that allows customization of text, font size, alignment, and color.

        :param text: The text to display on the label.
        :param font_size: The font size of the text (default: 12).
        :param alignment: The alignment of the text within the label (default: left aligned).
        :param color: The color of the text (default: black).
        """
        super().__init__(text, parent)

        # Set the font size
        self.setFont(QFont("Arial", font_size))

        # Set the text alignment
        self.setAlignment(alignment)

        # Set the text color
        self.setStyleSheet(f"color: {color};")
