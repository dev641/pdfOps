from reportlab.platypus import (
    Table,
    TableStyle,
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from .table import TableReporter
from common.Settings import MAIN_HEADER_TEXT_FOR_REPORT


class ReportLab:
    def __init__(
        self,
        page_size=A4,
        rightMargin=10,
        leftMargin=10,
        topMargin=10,
        bottomMargin=10,
        margin=10,
    ):
        self.page_width, self.page_height = page_size
        self.margin = margin
        self.usage_width = self.get_usage_width(
            margin=margin, leftMargin=leftMargin, rightMargin=rightMargin
        )
        self.usage_height = self.get_usage_height(
            margin=margin, topMargin=topMargin, bottomMargin=bottomMargin
        )
        self.main_header = self.generate_main_header(
            main_header_text=MAIN_HEADER_TEXT_FOR_REPORT
        )

        self.table_reporter = TableReporter()

    def get_document(
        self,
        outputFilePath: str,
        page_size=A4,
        rightMargin=10,
        leftMargin=10,
        topMargin=10,
        bottomMargin=10,
        showBoundary=False,
        margin=10,
    ):
        return SimpleDocTemplate(
            filename=outputFilePath,
            pagesize=page_size,
            rightMargin=rightMargin,
            leftMargin=leftMargin,
            topMargin=topMargin,
            bottomMargin=bottomMargin,
            showBoundary=showBoundary,
        )

    def get_usage_width(
        self, margin: int, leftMargin: int, rightMargin: int
    ) -> int:
        if leftMargin and rightMargin:
            return self.page_width - leftMargin - rightMargin
        return self.page_width - 2 * margin

    def get_usage_height(
        self, margin: int, topMargin: int, bottomMargin: int
    ) -> int:
        if topMargin and bottomMargin:
            return self.page_height - topMargin - bottomMargin
        return self.page_height - 2 * margin

    def generate_main_header(self, main_header_text):
        main_header_style = getSampleStyleSheet()["Title"]
        main_header = Paragraph(main_header_text, main_header_style)
        return main_header

    def generate_report(self, data, outputFilePath):
        document = self.get_document(outputFilePath=outputFilePath)
        main_header = self.main_header
        [table_data, total_page_data] = data
        table = self.generate_table(table_data)
        total_page_table = self.generate_table(total_page_data)
        space_after_table = Spacer(1, 18)  # 1 inch wide, 18 points tall

        document.build(
            [main_header, table, space_after_table, total_page_table]
        )

    def generate_table(self, data):
        return self.table_reporter.generate_table(
            data=data,
            page_width=self.usage_width,
            page_height=self.usage_height,
        )
