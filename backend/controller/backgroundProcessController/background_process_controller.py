from pathlib import Path
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox
from frontend.components.ProgressDialog.progress_dialog import ProgressDialog
from backend.services.backgroundProccessors.print_friendly_batch_service import (
    PrintFriendlyBatchService,
)
from backend.controller.baseTasks.base_tasks_controller import (
    BaseTaskController,
)


class BackgroundProcessController(BaseTaskController):

    def __init__(self, parent=None):
        super().__init__(parent)

    def update_src_folder(self, src_folder):
        self.src_folder = src_folder

    def on_folders_selected(self, dest_folder):

        total = len(self.src_folder)

        if total == 0:
            QMessageBox.information(
                self.parent,
                "No PDFs Found",
                "No PDF files were found.",
            )
            return
        print(
            f"Starting background process with source: {self.src_folder} and destination: {dest_folder}"
        )
        service = PrintFriendlyBatchService(
            pdf_list=self.src_folder, output_dir=dest_folder
        )

        self.start_service(service, total_files=total)
