from pathlib import Path
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox
from frontend.components.ProgressDialog.progress_dialog import ProgressDialog
from backend.services.flattenFolder.flatten_folder_service import (
    FlattenFolderService,
)
from backend.controller.baseTasks.base_tasks_controller import (
    BaseTaskController,
)


class FlattenFolderController(BaseTaskController):

    def on_folders_selected(self, src_folder, dest_folder):

        total = len(list(Path(src_folder).rglob("*.pdf")))

        if total == 0:
            QMessageBox.information(
                self.parent,
                "No PDFs Found",
                "No PDF files were found.",
            )
            return

        service = FlattenFolderService(src_folder, dest_folder)

        self.start_service(service, total_files=total)
