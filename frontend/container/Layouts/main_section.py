from frontend.container.pages.main import MainPage
from frontend.container.Layouts.layout_widget import VerticalLayoutWidget
from backend.controller.flattenFolder.flatten_folder_controller import (
    FlattenFolderController,
)
from backend.controller.backgroundProcessController.background_process_controller import (
    BackgroundProcessController,
)
from frontend.components.FolderSelector.folder_selector import FolderSelector
from common.enums.enums import PageEnum
from common.enums.enums import ActionType

# from common.utils.debug_layout_structure import debug_layout


class MainSectionWidget(VerticalLayoutWidget):
    def __init__(self):
        super().__init__()
        self.createMainSection()
        self.setup()
        self.connectFolderSelector()

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
        # Set the layout for this widget
        self.setLayout(self.layout)

    def connectFolderSelector(self):
        self.folder_selector.foldersSelected.connect(self.onFolderSelected)

    def setup(self):
        self.folder_selector = FolderSelector(self)
        self.flatten_controller = FlattenFolderController(self)
        self.background_process_controller = BackgroundProcessController(self)
        self.connectBackgroundProcessSignals()

    def getDragDropWidget(self):
        return self.widget.getPageByPageId(
            PageEnum.DRAG_DROP_FILE_PAGE.name
        ).widget

    def connectBackgroundProcessSignals(self):
        dragDropWidget = self.getDragDropWidget()
        dragDropWidget.fileSignal.connect(
            self.background_process_controller.update_src_folder
        )

    def dispatchAction(self, actionType):
        dragDropWidget = self.getDragDropWidget()

        if actionType == ActionType.CREATE_PDF:
            dragDropWidget.saveFile()
        elif actionType == ActionType.MERGE_PDF:
            dragDropWidget.mergePdfs()
        elif actionType == ActionType.FLATTEN_FOLDER:
            self.folder_selector.chooseSourceAndDestination(
                action=ActionType.FLATTEN_FOLDER
            )
        elif actionType == ActionType.CONVERT_TO_PRINT_FRIENDLY_PDF:
            self.folder_selector.chooseSourceAndDestination(
                sourceRequired=False,
                action=ActionType.CONVERT_TO_PRINT_FRIENDLY_PDF,
            )
        elif actionType == ActionType.SELECT_RATE:
            dragDropWidget.calculate_cost()
        else:
            pageId = PageEnum[actionType.value].name
            self.widget.switchPage(pageId)

    def onFolderSelected(
        self, sourceFolder: str, destinationFolder: str, action
    ):
        if action == ActionType.FLATTEN_FOLDER:
            print(
                f"Flattening folder. Source: {sourceFolder}, Destination: {destinationFolder}"
            )
            self.flatten_controller.on_folders_selected(
                sourceFolder, destinationFolder
            )
        elif action == ActionType.CONVERT_TO_PRINT_FRIENDLY_PDF:
            print(
                f"Converting to Print-Friendly PDF. Source: {sourceFolder}, Destination: {destinationFolder}"
            )
            self.background_process_controller.on_folders_selected(
                destinationFolder
            )
