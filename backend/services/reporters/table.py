from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, PageBreak


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
                    12,
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

    def get_column_width(self, page_width: float, num_columns: int) -> float:
        return page_width / num_columns

    def generate_table(self, data, page_width, page_height) -> Table:
        table = Table(
            data=data,
            # rowHeights=[25] * len(data),
            colWidths=self.get_column_width(
                page_width=page_width, num_columns=len(data[0])
            ),
            splitByRow=True,
            repeatRows=True,
        )
        table.setStyle(self.get_stylesheet())
        return table
