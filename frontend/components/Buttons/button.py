from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt


class Button(QPushButton):
    def __init__(
        self,
        text,
        parent=None,
        styleSheet: str = None,
        onClick: callable = None,
    ):
        super().__init__(text, parent)
        self.onClick = onClick
        # Customize the button's appearance and behavior
        if styleSheet:
            self.setStyleSheet(styleSheet)
        else:
            self.setStyleSheet(
                """
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
            """
            )
        self._disableButton()
        # Optionally, connect signals to custom methods
        self.clicked.connect(self.onClick)

    def setButtonStyle(
        self,
        backgroundColor: str,
        textColor: str,
        overrideStyle: bool = False,
        styleSheet: str = None,
    ):
        """Method to change button's style dynamically."""
        if overrideStyle:
            self.setStyleSheet(styleSheet)
        else:
            self.setStyleSheet(
                f"""
                background-color: {backgroundColor};
                color: {textColor};
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
            """
            )

    def _disableButton(
        self, backgroundColor: str = "gray", textColor: str = "white"
    ):
        self.setEnabled(False)
        self.setButtonStyle(
            backgroundColor=backgroundColor, textColor=textColor
        )
        self.setCursor(Qt.ForbiddenCursor)

    def _enableButton(
        self, backgroundColor: str = "#4CAF50", textColor: str = "white"
    ):
        self.setEnabled(True)
        self.setButtonStyle(
            backgroundColor=backgroundColor, textColor=textColor
        )
        self.setCursor(Qt.PointingHandCursor)

    def enableButton(self, enable: bool = True):
        if enable:
            self._enableButton()
        else:
            self._disableButton()
