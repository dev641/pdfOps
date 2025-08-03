from ..Layouts.layout_widget import VerticalLayoutWidget
from frontend.components.TableView.table_view import TableView
from frontend.components.Buttons.button import Button
from PySide6.QtGui import QColor, QFont
from common.models.data_model import Data
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QSizePolicy, QSpacerItem
from .page import Page
from backend.services.reporters.report_lab import ReportLab
from backend.services.processors.pdf_processor import PDFProcessor
from common.models.summary_modal import SummaryModal
from frontend.container.Layouts.splitter import Splitter

# from common.utils.debug_layout_structure import debug_layout


class ContentPage(Page):
    enableButtonsSignal = Signal(bool)

    def __init__(
        self,
        pageId: str = "",
        pageTitle: str = "",
    ):
        super().__init__(pageId, pageTitle)
        self.setWindowTitle(pageTitle)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table = TableView(enableRowDrag=True)
        # self.table.setMinimumHeight(500)
        self.summaryTable = TableView()
        self.reportLab = ReportLab()
        self.setHeaders()
        # debug_layout(self)

    def createSplitter(self):
        # debug_layout(self)
        # debug_layout(self.table)
        # debug_layout(self.summaryTable)
        self.widget = Splitter(
            widget_1=self.table,
            widget_2=self.summaryTable,
            orientation=Qt.Vertical,
            stretch_factor=[7, 3],
        )
        # self.addItem(
        #     QSpacerItem(200, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # )
        self.addWidget(
            self.widget,
        )

    def createContent(self, rowData: list[Data] = []):
        self.appendAllRows(rowData)
        self.table.resizeTableToFitContent(column=True, row=True)
        self.summaryTable.resizeTableToFitContent(column=True)
        self.createSplitter()
        self.setLayout(self.layout)

    def setHeaders(self):
        # Define the headers for the table
        headers = Data.get_all_fields(Data)
        headers.append("Actions")
        self.table.addHeaders(headers)
        # Define total table headers
        headers = SummaryModal.get_all_fields(SummaryModal)
        self.summaryTable.addHeaders(headers)
        self.table.setColumnsWidth(ratios=[4, 1, 1])

    def addRow(self, rowData: Data = None):
        styles = [
            {"foreground": QColor("blue")},
            {"font": QFont("Arial", 12, QFont.Bold)},
            {"background": QColor("lightgray")},
        ]
        self.table.addRow(rowData)

    def resetAllRows(self):
        self.table.removeAllRows()
        self.summaryTable.removeAllRows()

    def appendAllRows(self, rowData: list[Data] = None):
        if not rowData:
            return

        self.resetAllRows()
        summaryModal = SummaryModal()
        for row in rowData:
            summaryModal.total_pages += row.page_count
            self.addRow(row)
        self.addRowsToSummaryTable(summaryModal)

    def updateRate(self, rate):
        total_page = float(self.summaryTable.getCellText(row=0, col=0))
        self.summaryTable.updateRow(row=0, col=1, value=rate)
        if total_page:
            self.summaryTable.updateRow(row=0, col=2, value=rate * total_page)

    def addRowsToSummaryTable(self, total_page_model: SummaryModal):
        self.summaryTable.addRow(total_page_model)

    def removeLastRow(self):
        last_rowIndex = self.table.rowCount() - 1
        self.table.removeRowAtIndex(last_rowIndex)

    def onFileHandleComplete(self):
        self.table.dragDropFile.onComplete()

    def fetchAllData(self):
        header = self.table.fetchHeaders()
        header = ["Serial No"] + header
        table = self.table.fetchAllRows(needIndex=True)
        table.insert(0, header)
        header = self.summaryTable.fetchHeaders()
        summaryTable = self.summaryTable.fetchAllRows()
        summaryTable.insert(0, header)
        return [table, summaryTable]

    def saveFile(self, outputFilePath: str = ""):
        data = self.fetchAllData()
        self.reportLab.generate_report(
            data=data, outputFilePath=outputFilePath
        )

    def mergePdfs(
        self,
        pdfFiles: list[str],
        outputFilePath: str = "",
        add_blank_page: bool = False,
    ):
        PDFProcessor.mergePdfs(
            pdfFiles=pdfFiles,
            outputFile=outputFilePath,
            add_blank_page=add_blank_page,
        )
