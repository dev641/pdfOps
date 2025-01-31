from PySide6.QtWidgets import QComboBox, QWidget
from PySide6.QtCore import Qt


class ComboBox(QComboBox):
    def __init__(
        self,
        items=None,
        parent=None,
        onItemSelected: callable = None,
        width=200,
        height=40,
    ):
        """
        Custom QComboBox class.

        :param items: A list of items to populate the combo box.
        :param parent: The parent widget (optional).
        """
        super().__init__(parent)
        self.onItemSelected = onItemSelected
        self.setFixedSize(width, height)
        # Add label item as a placeholder
        self.addItem("Select an option:")
        self.setItemData(
            0, 0, Qt.UserRole - 1
        )  # Disable selection for the first item
        self.setStyleSheet(
            """
                    QComboBox {
                        padding: 10px;  /* 10px padding on all sides */
                    }
                """
        )
        if items:
            self.addItems(items)

        # Customize combo box appearance and behavior
        self.setEditable(False)  # Make it non-editable
        self.setMaxVisibleItems(5)  # Set maximum visible items in dropdown
        self.activated.connect(self.onItemSelected)
