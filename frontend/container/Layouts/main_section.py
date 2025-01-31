from frontend.container.pages.main import MainPage
from frontend.container.Layouts.layout_widget import VerticalLayoutWidget
from common.enums.enums import PageEnum
from common.enums.enums import ActionType

# from common.utils.debug_layout_structure import debug_layout


class MainSectionWidget(VerticalLayoutWidget):
    def __init__(self):
        super().__init__()
        self.createMainSection()
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

    def navigateToPage(self, actionType):
        dragDropWidget = self.widget.getPageByPageId(
            PageEnum.DRAG_DROP_FILE_PAGE.name
        ).widget
        if actionType == ActionType.CREATE_PDF:
            dragDropWidget.saveFile()
        elif actionType == ActionType.MERGE_PDF:
            dragDropWidget.mergePdfs()
        elif actionType == ActionType.SELECT_RATE:
            dragDropWidget.calculate_cost()
        else:
            pageId = PageEnum[actionType.value].name
            self.widget.switchPage(pageId)
