from PySide6.QtWidgets import (
    QStackedWidget,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QDialog,
)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy

# Set the widget's size policy to fixed


class VerticalLayoutWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.layout = QVBoxLayout()

    def addWidget(self, widget: QWidget, alignment=None, stretch=None) -> None:
        """Add a widget to the layout."""
        if alignment is not None and stretch is not None:
            self.layout.addWidget(widget, alignment=alignment, stretch=stretch)
        if alignment is not None:
            self.layout.addWidget(widget, alignment=alignment)
        if stretch is not None:
            self.layout.addWidget(widget, stretch=stretch)
        else:
            self.layout.addWidget(widget)

    def addItem(self, item) -> None:
        """Add an item to the layout."""
        self.layout.addItem(item)

    def removeWidget(self, widget: QWidget) -> None:
        """Remove a widget from the layout."""
        self.layout.removeWidget(widget)


class HorizontalLayoutWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()

    def addWidget(self, widget: QWidget, alignment=None) -> None:
        """Add a widget to the layout."""
        if alignment is not None:
            self.layout.addWidget(widget, alignment=alignment)
        else:
            self.layout.addWidget(widget)

    def removeWidget(self, widget: QWidget) -> None:
        """Remove a widget from the layout."""
        self.layout.removeWidget(widget)


class StackWidget(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Create the layout that will hold the stacked widget
        self.layout = QVBoxLayout()

    def addPage(self, page: QWidget) -> None:
        """Dynamically add a page to the stacked widget."""
        self.addWidget(page)

    def addWidgetToLayout(self, widget: QWidget, alignment=None) -> None:
        """Add a widget to the layout."""
        if alignment is not None:
            self.layout.addWidget(widget, alignment=alignment)
        else:
            self.layout.addWidget(widget)

    # def set_current_index(self, index: int) -> None:
    #     """Set the current widget by index."""
    #     self.setCurrentIndex(index)


class VerticalDialogWidget(QDialog):

    def __init__(self, parent=None):
        super().__init__()
        self.layout = QVBoxLayout()

    def addWidget(self, widget: QWidget, alignment=None) -> None:
        """Add a widget to the layout."""
        if alignment is not None:
            self.layout.addWidget(widget, alignment=alignment)
        else:
            self.layout.addWidget(widget)

    def removeWidget(self, widget: QWidget) -> None:
        """Remove a widget from the layout."""
        self.layout.removeWidget(widget)
