from frontend.container.pages.main import MainPage
from frontend.container.Layouts.layout_widget import VerticalLayoutWidget
from frontend.container.flattenFolder.flatten_folder_controller import (
    FlattenFolderController,
)
from frontend.components.FolderSelector.folder_selector import FolderSelector
from common.enums.enums import PageEnum
from common.enums.enums import ActionType
from frontend.components.Printer.print_manager import PrintManager

# from common.utils.debug_layout_structure import debug_layout


class MainSectionWidget(VerticalLayoutWidget):
    filePaths = []

    def __init__(self):
        super().__init__()
        self.createMainSection()
        self.setupFlattenFolder()
        self.setupPrintManager()
        # debug_layout(self)
        # self.setStyleSheet("background-color: #90EE90;")  # Light Green

    def createMainSection(self):
        # Create the layout for the right section
        self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        self.widget = MainPage(
            pageId=PageEnum.MAIN_PAGE.name,
            pageTitle=PageEnum.MAIN_PAGE.value,
        )
        self.addWidget(self.widget)
        self.connectWithFileSignal()
        # Set the layout for this widget
        self.setLayout(self.layout)

    def setupPrintManager(self):
        self.printManager = PrintManager(
            self, file_list_getter=self.getFilePaths
        )

    def setupFlattenFolder(self):
        self.folder_selector = FolderSelector(self)
        self.flatten_controller = FlattenFolderController(self)
        self.folder_selector.foldersSelected.connect(
            self.flatten_controller.on_folders_selected
        )

    def connectWithFileSignal(self):
        dragDropWidget = self.widget.getDragDropWidget()
        dragDropWidget.fileSignal.connect(self.setFilePaths)

    def setFilePaths(self, filePaths: list):
        self.filePaths = filePaths

    def getFilePaths(self):
        if self.filePaths:
            return self.filePaths
        return None

    def dispatchAction(self, actionType):
        dragDropWidget = self.widget.getPageByPageId(
            PageEnum.DRAG_DROP_FILE_PAGE.name
        ).widget

        if actionType == ActionType.CREATE_PDF:
            dragDropWidget.saveFile()
        elif actionType == ActionType.MERGE_PDF:
            dragDropWidget.mergePdfs()
        elif actionType == ActionType.FLATTEN_FOLDER:
            self.folder_selector.chooseSourceAndDestination()
        elif actionType == ActionType.PRINT_PDF:
            self.printManager.triggerPrintAll()
        elif actionType == ActionType.SELECT_RATE:
            dragDropWidget.calculate_cost()
        else:
            pageId = PageEnum[actionType.value].name
            self.widget.switchPage(pageId)
