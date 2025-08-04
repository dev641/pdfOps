from PySide6.QtWidgets import (
    QTableWidget,
    QHeaderView,
    QSizePolicy,
    QAbstractScrollArea,
)
from PySide6.QtCore import Qt, QMimeData, Signal
from .table_cell import (
    TableCellTextItem,
    DeleteCell,
)
from PySide6.QtGui import QDrag
from common.utils.utils import CaseConverter
from common.enums.enums import CaseType
from frontend.components.FileSelector.drag_drop_selection import (
    DragDropSelection,
)


class TableView(QTableWidget):
    fileProcessingSignal = Signal(list)
    onRowChangeSignal = Signal(bool)
    removeRowSignal = Signal(int)

    def __init__(
        self,
        parent=None,
        enableRowDrag=False,
        enableSorting=False,
        resizeMode: QHeaderView.ResizeMode = QHeaderView.ResizeMode.Stretch,
        values: list[int] = None,
    ):
        super().__init__(parent)
        self.dragDropFile = DragDropSelection()
        self.enableSorting = enableSorting
        self.setup(enableRowDrag)
        self.resizeMode = resizeMode
        self.values = values

    def setup(self, enableRowDrag: bool):
        """Setup the table with 0 rows and no columns."""
        self.setRowCount(0)
        self.setColumnCount(0)
        if self.enableSorting:
            self.setSortingEnabled(True)
        if enableRowDrag:
            self.enableRowDrag()
        self.clear()

    def enableRowDrag(self):
        """Enable row drag and drop functionality"""
        # Enable drag-and-drop
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(
            QTableWidget.InternalMove
        )  # Allow row rearrangement

    def fetchAllRows(self, needIndex: bool = False) -> list[list]:
        """
        Fetch all rows from the table.
        """
        rows = []
        for rowIndex in range(self.rowCount()):
            row = [rowIndex + 1] if needIndex else []
            for colIndex in range(self.columnCount()):
                item = self.item(rowIndex, colIndex)
                if item is not None:
                    row.append(item.text())
            rows.append(row)

        return rows

    def getCellText(self, row, col):
        """
        Get the text from a specific cell in the table.
        """
        item = self.item(row, col)
        if item is not None:
            return item.text()
        else:
            return None  # Return None if the cell is empty or does not exist

    def updateRow(self, row, col, value):
        """
        Update a cell in the table.
        If the cell does not exist, create a new item.
        """
        item = self.item(row, col)
        if item is None:
            # Create a new item if it doesn't exist
            item = TableCellTextItem(str(value))
            self.setItem(row, col, item)  # Add the item to the table
        else:
            # If the item already exists, just update the text
            item.setText(str(value))

    def fetchHeaders(self) -> list:
        """
        Fetch the table headers.
        """
        headers = []
        for colIndex in range(self.columnCount()):
            item = self.horizontalHeaderItem(colIndex)
            if item is not None and item.text() != "Actions":
                (
                    headers.append(
                        CaseConverter.convert(
                            input_string=item.text(),
                            target_case=CaseType.CAPITALIZED_WORDS,
                        )
                    )
                )
        return headers

    def onItemChange(self, item=None):
        self.onRowChangeSignal.emit(self.rowCount() > 0)
        # print("Item changed:", item)

    def addHeaders(self, columns):
        """
        Initialize table headers.

        :param columns: List of column headers to set in the table.
        """

        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(
            [
                CaseConverter.convert(
                    input_string=col, target_case=CaseType.CAPITALIZED_WORDS
                )
                for col in columns
            ]
        )

    def addRow(self, rowData):
        """
        Add a row to the table at the end.

        :param rowData: List of values to add to the row.
        """
        if self.enableSorting:
            self.setSortingEnabled(False)

        rowIndex = self.rowCount()
        self.insertRow(rowIndex)

        for colIndex, (_, value) in enumerate(rowData):
            item = TableCellTextItem(text=str(value), alignment=Qt.AlignCenter)
            self.setItem(rowIndex, colIndex, item)
        self.addDeleteButtonCell(rowIndex, len(rowData))
        self.onItemChange(item=None)

        if self.enableSorting:
            self.setSortingEnabled(True)

    def addDeleteButtonCell(self, rowIndex, colIndex):
        """
        Add a delete cell to the last column of the specified row.
        """
        # Add the delete button in the "Actions" column
        delete_cell = DeleteCell(rowIndex)
        delete_cell.layout.setAlignment(Qt.AlignCenter)
        delete_cell.cellSignal.connect(self.removeRowAtIndex)
        self.setCellWidget(rowIndex, colIndex, delete_cell)

    def removeRowAtIndex(self, rowIndex):
        """
        Remove a row from the table.

        :param rowIndex: Index of the row to remove.
        """
        if 0 > rowIndex >= self.rowCount():
            raise IndexError(f"Row index {rowIndex} is out of range.")
        self.removeRow(rowIndex)
        # Update remaining row indices for delete cells
        for i in range(self.rowCount()):
            cell_widget = self.cellWidget(i, self.columnCount() - 1)
            if isinstance(cell_widget, DeleteCell):
                cell_widget.updateRowIndex(i)
        self.onItemChange(item=None)
        self.removeRowSignal.emit(rowIndex)

    def removeAllRows(self):
        self.setRowCount(0)

    def resizeColumnsToStretch(self, header: QHeaderView, column_count: int):
        for col in range(column_count):
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)

    def resizeColumnsToCustom(
        self, header: QHeaderView, column_count: int, ratios: list[int] = None
    ):
        width = self.viewport().width()
        total = sum(ratios)
        if total == 0:
            ValueError("ratios sum shouldn't be 0")
        for i in range(column_count):
            header.setSectionResizeMode(i, QHeaderView.Custom)
            header.resizeSection(i, int((ratios[i] / total) * width))

    def resizeColumnsToFixed(
        self, header: QHeaderView, column_count: int, values: list[int] = None
    ):
        for i in range(column_count):
            header.setSectionResizeMode(i, QHeaderView.Fixed)
            header.resizeSection(i, values[i])

    def resizeTableToFitContent(
        self,
        values: list[int] = None,
        resizeMode: QHeaderView.ResizeMode = QHeaderView.ResizeMode.Stretch,
    ):
        if resizeMode and values:
            self.resizeColumns(resizeMode=resizeMode, values=values)
        else:
            self.resizeColumns(resizeMode=self.resizeMode, values=self.values)
        self.updateGeometry()

    def resizeColumns(
        self, resizeMode: QHeaderView.ResizeMode, values: list[int] = None
    ):
        if not resizeMode:
            return
        column_count = self.columnCount()
        header = self.horizontalHeader()
        if resizeMode == QHeaderView.ResizeMode.Stretch:
            self.resizeColumnsToStretch(
                header=header, column_count=column_count
            )
        elif resizeMode == QHeaderView.ResizeMode.Custom and values:
            self.resizeColumnsToCustom(
                header=header, column_count=column_count, ratios=values
            )
        elif resizeMode == QHeaderView.ResizeMode.Fixed and values:
            self.resizeColumnsToFixed(
                header=header, column_count=column_count, values=values
            )
        elif resizeMode == QHeaderView.ResizeMode.ResizeToContents:
            self.resizeColumnsToContents()

    def onSectionResized(self, logicalIndex, oldSize, newSize):
        # Handle custom resizing logic, for example, adjusting other columns or enforcing min/max sizes
        print(f"Column {logicalIndex} resized from {oldSize} to {newSize}")

        # Optionally, apply custom logic like limiting resizing to certain ranges or adjusting the sizes based on other columns
        if newSize < 50:  # Set a minimum width for columns
            self.table.horizontalHeader().resizeSection(logicalIndex, 50)
        elif newSize > 300:  # Set a maximum width for columns
            self.table.horizontalHeader().resizeSection(logicalIndex, 300)

    def dragEnterEvent(self, event):
        # Allow dragging into this widget
        if event.mimeData().hasUrls():
            self.dragDropFile.dragEnterEvent(event)
        else:
            if event.mimeData():
                event.accept()
            else:
                event.ignore()

    def dragMoveEvent(self, event):
        # Accept movement while dragging
        event.accept()

    def startDrag(self, actions):
        # Get the row being dragged
        self.dragged_row = self.currentRow()

        # Create a drag object
        drag = QDrag(self)
        mime_data = QMimeData()
        drag.setMimeData(mime_data)
        drag.exec(Qt.MoveAction)

    def resizeEvent(self, event):
        # self.set_column_width_ratio([2, 1, 3])
        self.resizeTableToFitContent()
        super().resizeEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            self.dragDropFile.dropEvent(event)
            self.onDragComplete()
            return
        # Get the drop position
        drop_row = self.indexAt(event.pos()).row()

        if drop_row == -1:  # If no valid drop row, default to the last row
            drop_row = self.rowCount() - 1

        # Extract data from the dragged row
        # Extract data from the dragged row
        dragged_data = []
        dragged_widgets = []

        for col in range(self.columnCount()):
            # Check if the cell contains a widget
            widget = self.cellWidget(self.dragged_row, col)
            if widget:
                dragged_widgets.append((col, widget))
            else:
                item = self.item(self.dragged_row, col)
                dragged_data.append((col, item.text() if item else ""))

        # Remove the original row
        self.removeRowAtIndex(self.dragged_row)

        # Insert the dragged row's data into the drop position
        self.insertRow(drop_row)
        # Add the text data back to the new row
        for col, data in dragged_data:
            self.setItem(
                drop_row,
                col,
                TableCellTextItem(text=data, alignment=Qt.AlignCenter),
            )

        # Add the widgets back to the new row
        self.addDeleteButtonCell(drop_row, dragged_widgets[0][0])

        # Refresh the rows
        # self.resizeRowsToContents()

        # Accept the event
        event.accept()

    def onDragComplete(self):
        self.fileProcessingSignal.emit(self.dragDropFile.filePaths())
        print("Dragging complete!")
