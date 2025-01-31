from ..Layouts.layout_widget import VerticalLayoutWidget, StackWidget
from .drag_drop_file_page import DragDropFilePage
from .page import Page
from frontend.components.Buttons.button import Button
from .content_page import ContentPage
from backend.services.processors.pdf_processor import PDFProcessor
from common.enums.enums import PageEnum
from PySide6.QtWidgets import QWidget

# from common.utils.debug_layout_structure import debug_layout


class MainPage(Page):
    def __init__(self, pageId: str, pageTitle: str):
        super().__init__(pageId=pageId, pageTitle=pageTitle)
        self.stack_widget = StackWidget()
        self.pages = []
        # Create the pages
        self.createAllPage()
        self.connectComponents()
        self.addWidget(self.stack_widget)
        self.setLayout(self.layout)
        # debug_layout(self)

    def addPageToStack(self, page: Page) -> None:
        self.pages.append(page)
        self.stack_widget.addPage(page)

    def setCurrentPage(self, pageId: str) -> None:
        index = self.findIndexByPageId(pageId=pageId)
        # Set the initial page
        self.stack_widget.setCurrentWidget(self.pages[index])

    def createAllPage(self) -> None:
        # Add the Drag and drop pages to the stack widget
        self.addPageToStack(
            page=DragDropFilePage(
                pageId=PageEnum.DRAG_DROP_FILE_PAGE.name,
                pageTitle=PageEnum.DRAG_DROP_FILE_PAGE.value,
            )
        )

        self.addPageToStack(
            page=ContentPage(
                pageId=PageEnum.CONTENT_PAGE.name,
                pageTitle=PageEnum.CONTENT_PAGE.value,
            )
        )

    def processPdfs(self, filePaths: str) -> None:
        data = []
        for file_path in filePaths:
            data.append(self.processPdf(file_path))

        pageId = PageEnum.CONTENT_PAGE.name
        # fetch content page index to invoke createContent method
        contentIndex = self.findIndexByPageId(pageId=pageId)
        # Update the content page with the processed data
        self.pages[contentIndex].createContent(
            data
        )  # Update the content page with the processed data
        self.switchPage(pageId=pageId)

    def processPdf(self, file_path) -> None:
        return PDFProcessor.process_data(file_path)

    def findIndexByPageId(self, pageId) -> int:
        return next(
            (i for i, item in enumerate(self.pages) if item.pageId == pageId),
            -1,
        )

    def switchPage(self, pageId: str) -> None:
        """Switch to the next page in the stacked widget."""
        desiredIndex = self.findIndexByPageId(pageId)
        # Set the desired page
        self.stack_widget.setCurrentIndex(desiredIndex)

    def getPageByPageId(self, pageId) -> Page:
        index = self.findIndexByPageId(pageId)
        return self.pages[index]

    def connectComponents(self):
        dragDropIndex = self.findIndexByPageId(pageId=PageEnum.DRAG_DROP_FILE_PAGE.name)
        contentIndex = self.findIndexByPageId(pageId=PageEnum.CONTENT_PAGE.name)
        dragDropWidget = self.pages[dragDropIndex].widget
        contentPageWidget = self.pages[contentIndex]
        # connect the signal from the drag and drop widget and table to process pdfs
        dragDropWidget.fileSignal.connect(self.processPdfs)
        contentPageWidget.table.fileProcessingSignal.connect(self.processPdfs)
        dragDropWidget.saveFileSignal.connect(self.pages[contentIndex].saveFile)

        dragDropWidget.mergePdfsSignal.connect(self.pages[contentIndex].mergePdfs)
        dragDropWidget.pageRateSignal.connect(contentPageWidget.updateRate)
