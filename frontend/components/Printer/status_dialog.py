# frontend/status_dialog.py
from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QHBoxLayout,
)
from PySide6.QtCore import Qt
from frontend.components.TableView.table_view import TableView
from typing import Optional


class StatusDialog(QDialog):
    def __init__(
        self, files: list[str] = None, parent: Optional[QWidget] = None
    ):
        super().__init__(parent)
        self.setWindowTitle("Print Status")
        self.resize(800, 400)
        self.table = TableView()
        self.table.addHeaders(["File", "Status"])
        layout = QVBoxLayout(self)
        layout.addWidget(self.table)
        if files:
            for p in files:
                self.table.addRow([("File", p), ("Status", "Pending")])

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        bottom = QHBoxLayout()
        bottom.addStretch(1)
        bottom.addWidget(close_btn)
        layout.addLayout(bottom)

    def set_status(self, path: str, status_text: str):
        for r in range(self.table.rowCount()):
            item = self.table.item(r, 0)
            if item and item.text() == path:
                self.table.updateRow(row=r, col=1, value=status_text)
                break
