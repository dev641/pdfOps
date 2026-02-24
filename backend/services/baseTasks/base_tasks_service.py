from PySide6.QtCore import QObject, Signal


class BaseTaskService(QObject):
    progressChanged = Signal(int, int, str)
    finishedProcessing = Signal(int, int, bool)

    def stop(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError
