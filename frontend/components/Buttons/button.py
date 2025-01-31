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
