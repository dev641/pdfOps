from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QProgressBar,
    QHBoxLayout,
    QPushButton,
)
from ...container.Layouts.layout_widget import HorizontalLayoutWidget


class ProgressDialog(QDialog):
    def __init__(self, total_files: int, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Flattening PDFs…")
        self.setModal(True)

        self._total = max(1, total_files)

        self.label_title = QLabel("Processing files…", self)
        self.label_detail = QLabel("", self)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, self._total)
        self.progress_bar.setValue(0)

        self.cancel_button = QPushButton("Cancel", self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label_title)
        layout.addWidget(self.label_detail)
        layout.addWidget(self.progress_bar)

        row = QHBoxLayout()
        row.addStretch(1)
        row.addWidget(self.cancel_button)
        layout.addLayout(row)

        self.setMinimumWidth(420)

    def update_progress(self, processed: int, total: int, filename: str):
        self.progress_bar.setMaximum(max(1, total))
        self.progress_bar.setValue(processed)
        self.label_detail.setText(f"{processed}/{total}  •  {filename}")
