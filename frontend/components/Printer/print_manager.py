from PySide6.QtWidgets import QMessageBox, QWidget
from PySide6.QtCore import Slot, QObject, Signal
from .printer_dialog import PrintDialog
from .status_dialog import StatusDialog
from typing import Callable, Optional, List

from backend.controller.print.print_controller import PrintController
from common.enums.enums import JobStatus


class PrintManager(QObject):
    job_started = Signal(list)  # emits list of files
    job_finished = Signal()  # emits when batch done
    """
    Handles print-related UI and connects it to backend controller.
    Keeps MainWindow cleaner.
    """

    def __init__(
        self, parent_window: QWidget, file_list_getter: Callable[[], List[str]]
    ):
        """
        parent_window: the main window
        file_list_getter: callable to get current list of PDFs
        """
        super().__init__(parent=parent_window)
        self.parent_window = parent_window
        self.get_files = file_list_getter

        self.controller = PrintController()
        self.controller.progress.connect(self.on_progress)
        self.controller.finished.connect(self.on_finished)

        self.status_dialog: StatusDialog | None = None
        self.pd = PrintDialog(self.parent_window)

    def triggerPrintAll(self):
        files = self.get_files()
        if not files:
            QMessageBox.warning(
                self.parent_window,
                "No PDFs",
                "Please add at least one PDF to print.",
            )
            return

        # Show print settings dialog
        pd = PrintDialog(self.parent_window)
        if pd.exec() != PrintDialog.Accepted:
            return

        settings = pd.get_settings()
        if settings is None:
            QMessageBox.warning(
                self.parent_window,
                "Printer Required",
                "Please choose a printer via the OS dialog.",
            )
            return

        # Show status dialog
        self.status_dialog = StatusDialog(files, self.parent_window)
        self.status_dialog.show()

        # Start print job
        self.controller.start_batch_print(files, settings)

    @Slot(str, int, str)
    def on_progress(self, path: str, status_value: int, message: str):
        if not self.status_dialog:
            return
        status = JobStatus(status_value)
        if status == JobStatus.IN_PROGRESS:
            self.status_dialog.set_status(path, "Printing...")
        elif status == JobStatus.DONE:
            self.status_dialog.set_status(path, "✅ Done")
        elif status == JobStatus.ERROR:
            self.status_dialog.set_status(path, f"❌ {message}")

    @Slot()
    def on_finished(self):
        QMessageBox.information(
            self.parent, "Batch Print", "All print jobs processed."
        )
