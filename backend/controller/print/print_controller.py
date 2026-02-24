# backend/controller.py
from PySide6.QtCore import QObject, QThread, Signal, Slot
from backend.services.print.print_service import PrintService
from common.models.print.print_settings import PrinterSettings
from common.models.print.print_setting_dto import PrinterSettingsDTO
from backend.workers.print.print_worker import PrintWorker


class PrintController(QObject):
    progress = Signal(str, int, str)  # forwarded worker progress
    finished = Signal()

    def __init__(self, gs_path: str | None = None):
        super().__init__()
        self.service = PrintService(gs_path)
        self._thread = None
        self._worker = None

    @Slot(list, object)
    def start_batch_print(self, file_list: list[str], settings):
        if self._thread:
            # Already running a job — could queue or raise
            return

        # Convert settings dataclass (frontend) into DTO used by service
        dto = PrinterSettingsDTO(
            printer_name=settings.printer_name,
            paper_size=settings.paper_size,
            orientation=settings.orientation,
            color=settings.color,
            duplex=settings.duplex,
            page_range=settings.page_range,
        )

        self._thread = QThread()
        self._worker = PrintWorker(file_list, dto, self.service)
        self._worker.moveToThread(self._thread)

        # Connect worker signals to controller signals/UI
        self._worker.progress.connect(self.progress)
        self._worker.finished.connect(self._on_finished)

        # Start worker when thread starts
        self._thread.started.connect(self._worker.run)
        self._thread.start()

    def _on_finished(self):
        if self._thread:
            self._thread.quit()
            self._thread.wait()
            self._worker.deleteLater()
            self._thread.deleteLater()
        self._worker = None
        self._thread = None
        self.finished.emit()
