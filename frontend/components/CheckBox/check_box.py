from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Qt, Signal


class Checkbox(QCheckBox):
    """
    A custom checkbox that emits the row when toggled.
    """

    row_checked = Signal(
        int, bool
    )  # Signal to emit the row index and checked state

    def __init__(self, rowIndex, parent=None):
        super().__init__(parent)
        self.rowIndex = rowIndex  # Store the associated row index
        self.stateChanged.connect(self.emitRowState)

    def emitRowState(self, state):
        """
        Emits the row index and the checkbox state.
        """
        # Check if state is Qt.Checked or Qt.Unchecked
        is_checked = state == Qt.Checked
        self.row_checked.emit(self.rowIndex, is_checked)
