from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QMenuBar,
    QMenu,
    QMessageBox,
)
import sys
from PySide6.QtGui import QAction  # Import QAction from PySide6.QtGui
from PySide6.QtCore import Signal
from common.enums.enums import (
    FileMenu,
    PdfTools,
    GoToPage,
    ActionType,
)
from enum import Enum


# Define a custom MenuBar class
class MenuBar(QMenuBar):
    menuBarNavigationSignal = Signal(Enum)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupMenus()

    def setupMenus(self):
        # Edit menu

        self.setupFileMenu()
        self.setupPdfToolsMenu()

        self.setupGoToMenu()

    def setupAndConnectActions(
        self, menu: QMenu, actionType: str, on_triggered
    ):
        action = QAction(actionType, self)
        action.triggered.connect(on_triggered)
        menu.addAction(action)

    def setupFileMenu(self):
        # File menu
        fileMenu = self.addMenu(FileMenu.class_name())

        self.setupAndConnectActions(
            menu=fileMenu,
            actionType=FileMenu.OPEN.value,
            on_triggered=self.openFile,
        )

        self.setupAndConnectActions(
            menu=fileMenu,
            actionType=FileMenu.SAVE_AS.value,
            on_triggered=self.saveFile,
        )

        self.setupAndConnectActions(
            menu=fileMenu,
            actionType=FileMenu.EXIT.value,
            on_triggered=self.exitApp,
        )

    def setupPdfToolsMenu(self):
        # PDF Tools menu
        pdfToolsMenu = self.addMenu(PdfTools.class_name())

        # Add actions to the PDF Tools menu
        self.setupAndConnectActions(
            menu=pdfToolsMenu,
            actionType=PdfTools.MERGE.value,
            on_triggered=self.mergeFiles,
        )

        self.setupAndConnectActions(
            menu=pdfToolsMenu,
            actionType=PdfTools.FLATTEN.value,
            on_triggered=self.flattenFolder,
        )

    def setupGoToMenu(self):
        # Go to menu
        goToMenu = self.addMenu(GoToPage.class_name())
        self.setupAndConnectActions(
            menu=goToMenu,
            actionType=GoToPage.TABLE.value,
            on_triggered=self.goToTable,
        )

    def openFile(self):
        self.menuBarNavigationSignal.emit(ActionType.SELECT_DIRECTORY)

    def saveFile(self):
        self.menuBarNavigationSignal.emit(ActionType.CREATE_PDF)

    def exitApp(self):
        QApplication.instance().quit()

    def mergeFiles(self):
        print("Merge files menu")
        self.menuBarNavigationSignal.emit(ActionType.MERGE_PDF)

    def flattenFolder(self):
        print("Flatten folders menu")
        self.menuBarNavigationSignal.emit(ActionType.FLATTEN_FOLDER)

    def goToTable(self):
        self.menuBarNavigationSignal.emit(ActionType.GO_TO_TABLE)
