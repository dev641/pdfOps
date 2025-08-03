from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, PageBreak
from common.Settings import REPORTLAB_ROWS_PER_PAGE


class TableReporter:
    def __init__(self):
        pass

    def get_stylesheet(self) -> TableStyle:
        return TableStyle(
            [
                (
                    'BACKGROUND',
                    (0, 0),
                    (-1, 0),
                    (0.5, 0.5, 0.5),
                ),  # Header background
                (
                    'TEXTCOLOR',
                    (0, 0),
                    (-1, 0),
                    (1, 1, 1),
                ),  # Header text color (white)
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center all text
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
                (
                    'BOTTOMPADDING',
                    (0, 0),
                    (-1, -1),
                    2,
                ),  # Padding for the cells
                (
                    'GRID',
                    (0, 0),
                    (-1, -1),
                    0.5,
                    (0, 0, 0),
                ),  # Cell grid with black borders
            ]
        )

    def get_column_widths(
        self,
        page_width: float,
        ratios: list[float],
        divide_columns_equally: bool,
    ) -> list[float]:
        """Calculate column widths based on given ratios."""
        total_ratio = sum(ratios)
        return (
            page_width / len(ratios)
            if divide_columns_equally
            else [(r / total_ratio) * page_width for r in ratios]
        )

    def generate_table(
        self,
        data,
        page_width,
        page_height,
        ratios: list[float],
        divide_columns_equally=False,
    ) -> Table:
        table = Table(
            data=data,
            rowHeights=page_height / REPORTLAB_ROWS_PER_PAGE,
            colWidths=self.get_column_widths(
                page_width=page_width,
                ratios=ratios,
                divide_columns_equally=divide_columns_equally,
            ),
            splitByRow=True,
            repeatRows=True,
        )
        table.setStyle(self.get_stylesheet())
        return table
