from PySide6.QtWidgets import (
    QDialogButtonBox,
)


class DialogButtonBox(QDialogButtonBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.addDefaultButtons()

    def addDefaultButtons(self):
        # Add default buttons like Ok, Cancel
        self.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

    def remove_button(self, button):
        """Remove a button from the button box."""
        self.removeButton(button)
