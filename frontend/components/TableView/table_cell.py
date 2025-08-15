import re
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem
from frontend.container.Layouts.layout_widget import HorizontalLayoutWidget
from PySide6.QtCore import Signal
from frontend.components.Buttons.button import Button
from PySide6.QtGui import QColor


class TableCellTextItem(QTableWidgetItem):
    def __init__(
        self,
        alignment=Qt.AlignCenter,
        text="",
        editable: bool = False,
        color=None,
    ):
        super().__init__(text)
        self.setTextAlignment(alignment)
        # Optionally set a background color
        if color:
            self.setBackground(QColor(color))

        # Make item editable or non-editable based on the `editable` parameter
        if editable:
            self.setFlags(self.flags() | Qt.ItemIsEditable)  # Editable
        else:
            self.setFlags(self.flags() & ~Qt.ItemIsEditable)  # Non-editable

    def _sort_key(self):
        return [
            int(part) if part.isdigit() else part.lower()
            for part in re.split(r'(\d+)', self.text())
        ]

    def __lt__(self, other):
        return self._sort_key() < other._sort_key()

    def setData(self, role, value):
        if role == Qt.DisplayRole:
            # Custom logic to format the text (e.g., uppercase the text)
            value = value.upper()
        return super().setData(role, value)

    def setBackgroundColor(self, color):
        """Set a custom background color."""
        self.setBackground(QColor(color))

    def setForegroundColor(self, color):
        """Set a custom background color."""
        self.setForeground(QColor(color))


class TableCellWidgetItem(HorizontalLayoutWidget):
    cellSignal = Signal(int)

    def __init__(self, rowIndex, parent=None):
        super().__init__(parent)
        self.rowIndex = rowIndex

    def initUi(self, widget):
        """
        Sets up the delete button (with "X") inside the cell.
        """
        self.layout.setContentsMargins(0, 0, 0, 0)  # Remove padding/margins
        self.layout.setSpacing(0)  # Button with "X" text
        self.addWidget(widget)
        self.setLayout(self.layout)

    def emitCellSignal(self):
        """
        Emits the delete signal with the row index.
        """
        self.cellSignal.emit(self.rowIndex)

    def updateRowIndex(self, new_index):
        """
        Updates the row index, useful when rows are reordered or removed.
        """
        self.rowIndex = new_index


class DeleteCell(TableCellWidgetItem):
    """
    A custom widget for a delete button inside a table cell.
    Emits a signal when clicked, passing the row index to be deleted.
    """

    def __init__(self, rowIndex, parent=None, enabled=True):
        super().__init__(rowIndex=rowIndex, parent=parent)
        # self.setFixedWidth(50)
        self.styleSheet = """
            QPushButton {
                color: white;
                background-color: red;
                border: none;
                border-radius: 24px;
                padding: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """
        self.widget = Button(
            "X", styleSheet=self.styleSheet, onClick=self.emitCellSignal
        )
        self.widget._enableButton(backgroundColor="red", textColor="white")
        self.initUi(widget=self.widget)
