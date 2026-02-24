from PySide6.QtCore import QThread


class TaskRunner(QThread):
    def __init__(self, service, parent=None):
        super().__init__(parent)
        self.service = service
        self.service.moveToThread(self)

        # expose service signals directly
        self.progressChanged = self.service.progressChanged
        self.finishedProcessing = self.service.finishedProcessing

    def run(self):
        self.service.execute()

    def stop(self):
        self.service.stop()
