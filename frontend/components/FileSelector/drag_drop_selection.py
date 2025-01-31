from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QDragEnterEvent, QDropEvent
import os
from backend.controller.file_handler import FileHandler
from common.utils.utils import is_pdf


class DragDropSelection(QWidget, FileHandler):
    def __init__(self):
        super().__init__()
        # Set up the window for drag and drop
        self.setAcceptDrops(True)

    @staticmethod
    def isPdf(path):
        """Check if a given path is a PDF file."""
        return is_pdf(path)

    def dragEnterEvent(self, event: QDragEnterEvent):
        """Allow only PDF files from the dragged items."""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            filePaths = [url.toLocalFile() for url in urls]
            # Check if at least one valid PDF file is present
            if any(
                self.isPdf(path) for path in filePaths
            ):  # At least one valid PDF
                event.acceptProposedAction()  # Accept the drag
            else:
                event.ignore()  # Reject if no valid PDFs
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        """Handle only PDF files dropped."""
        droppedUrls = event.mimeData().urls()  # Get URLs of dropped items
        filePaths = [url.toLocalFile() for url in droppedUrls]

        # Filter to include only PDF files
        pdfFiles = [path for path in filePaths if self.isPdf(path)]

        if pdfFiles:
            self.handleFiles(pdfFiles)  # Process the valid PDFs
        else:
            print("No valid PDF files were dropped.")  # Optional feedback
