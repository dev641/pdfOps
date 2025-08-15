from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
)

from frontend.container.Layouts.menu_bar import MenuBar
from frontend.container.Layouts.splitter import Splitter

# from frontend.container.Layouts.status_bar import StatusBar
from frontend.container.Layouts.left_section import LeftSectionWidget
from frontend.container.Layouts.main_section import MainSectionWidget
from PySide6.QtCore import Qt
from common.enums.enums import PageEnum

# from common.utils.debug_layout_structure import debug_layout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # # Window title
        self.setWindowTitle("Pdf Ops Tools")
        self.setGeometry(100, 100, 1000, 700)
        self.setContentsMargins(0, 0, 0, 0)
        self.menuBar = MenuBar()

        self.setMenuBar(self.menuBar)
        self.leftWidget = LeftSectionWidget()
        self.mainWidget = MainSectionWidget()
        self.connectComponents()
        # Create a Custom QSplitter with the widgets and initial sizes
        self.splitter = Splitter(
            widget_1=self.leftWidget,
            widget_2=self.mainWidget,
            orientation=Qt.Horizontal,
        )
        # Set Splitter as Central Widget in QMainWindow
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.splitter)
        container.setLayout(layout)
        self.setCentralWidget(container)
        # Set the splitter as the central widget
        self.setCentralWidget(self.splitter)
        # # Create a label
        # debug_layout(self)

    def connectComponents(self):
        # Connect the select directory signal to the right widget switch page
        self.menuBar.menuBarNavigationSignal.connect(
            self.mainWidget.dispatchAction
        )
        self.leftWidget.leftSectionNavigationSignal.connect(
            self.mainWidget.dispatchAction
        )
        dragDropWidget = self.mainWidget.widget.getPageByPageId(
            PageEnum.DRAG_DROP_FILE_PAGE.name
        ).widget
        contentPageTableWidget = self.mainWidget.widget.getPageByPageId(
            PageEnum.CONTENT_PAGE.name
        ).table

        contentPageTableWidget.removeRowSignal.connect(
            dragDropWidget.removeFileAtIndex
        )
        contentPageTableWidget.onRowChangeSignal.connect(
            self.leftWidget.enableButtons
        )
