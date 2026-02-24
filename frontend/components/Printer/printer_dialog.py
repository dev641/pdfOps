# frontend/print_dialog.py
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QFormLayout,
    QSpinBox,
)
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from typing import Optional, Tuple
from common.models.print.print_settings import PrinterSettings
from frontend.components.ComboBox.comboBox import ComboBox
from frontend.components.CheckBox.check_box import Checkbox
from frontend.components.Buttons.button import Button
from frontend.components.Labels.label import LabeledText
from frontend.container.Layouts.layout_widget import HorizontalLayoutWidget


class PrintDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Print Settings")
        self._selected_printer = None
        self._os_from = None
        self._os_to = None
        self.printerLabel = LabeledText("No printer chosen", color="white")

        form = QFormLayout()

        self.printerButton = self.getPrinterButton()

        self.addPrintSize(form=form)

        self.addOrientation(form=form)

        self.addColor(form=form)

        self.addDuplex(form=form)

        self.pageRangeBox = self.generatePageRange()

        okBtn = self.getButton(text="Start", cb=self.accept)
        cancelBtn = self.getButton(text="Cancel", cb=self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(self.printerButton)
        layout.addWidget(self.printerLabel)
        group = QGroupBox("Advanced (optional)")
        group.setLayout(form)
        layout.addWidget(group)
        layout.addLayout(self.pageRangeBox)
        self.addOKAndCancelButtonToLayout(
            okBtn=okBtn, cancelBtn=cancelBtn, layout=layout
        )

    def _show_qt_printer_dialog(self):
        qp = QPrinter()
        dlg = QPrintDialog(qp, self)
        dlg.setWindowTitle("Select Printer (applies to all files)")
        if dlg.exec() == QPrintDialog.Accepted:
            self._selected_printer = qp.printerName()
            self._os_from = qp.fromPage() or None
            self._os_to = qp.toPage() or None
            self.printerLabel.setText(f"Printer: {self._selected_printer}")

    def getPrinterButton(self):
        printer_button = Button(
            "Choose Printer & Page Range (OS)", enabled=True
        )
        printer_button.clicked.connect(self._show_qt_printer_dialog)
        return printer_button

    def addPrintSize(self, form: QFormLayout):
        self.paper_cb = ComboBox()
        self.paper_cb.addItems(["a4", "letter", "legal"])
        form.addRow("Paper Size:", self.paper_cb)

    def addOrientation(self, form: QFormLayout):
        self.orientation_cb = ComboBox()
        self.orientation_cb.addItems(["Portrait", "Landscape"])
        form.addRow("Orientation:", self.orientation_cb)

    def addColor(self, form: QFormLayout):
        self.color_cb = Checkbox("Color")
        self.color_cb.setChecked(True)
        form.addRow("Color:", self.color_cb)

    def addDuplex(self, form: QFormLayout):
        self.duplex_cb = ComboBox()
        self.duplex_cb.addItems(["None", "Long-edge", "Short-edge"])
        form.addRow("Duplex:", self.duplex_cb)

    def generateSpinBox(self, low: int = 0, high: int = 10000, value: int = 0):
        spin = QSpinBox()
        spin.setRange(low, high)
        spin.setValue(value)
        return spin

    def addRangeBox(
        self, text: str, spinBox: QSpinBox, box: QHBoxLayout | QVBoxLayout
    ):
        box.addWidget(LabeledText(text=text))
        box.addWidget(spinBox)

    def generatePageRange(self):
        # Page range spinboxes informative (actual range comes from OS dialog)
        prange_box = QHBoxLayout()
        self._from_spin = self.generateSpinBox()
        self.addRangeBox(text="From", spinBox=self._from_spin, box=prange_box)
        self._to_spin = self.generateSpinBox()
        self.addRangeBox(text="To", spinBox=self._to_spin, box=prange_box)
        return prange_box

    def getButton(self, text: str, cb: callable):
        btn = Button(text=text, enabled=True)
        btn.setButtonStyle(
            overrideStyle=True,
            styleSheet="""
            padding: 4px 8px;
            """,
        )
        btn.clicked.connect(cb)
        return btn

    def addOKAndCancelButtonToLayout(
        self, okBtn: Button, cancelBtn: Button, layout: QVBoxLayout
    ):
        btn_row = QHBoxLayout()
        btn_row.addStretch(1)
        btn_row.addWidget(okBtn)
        btn_row.addWidget(cancelBtn)
        layout.addLayout(btn_row)

    def get_settings(self) -> Optional[PrinterSettings]:
        if not self._selected_printer:
            return None
        pr = PrinterSettings(
            printer_name=self._selected_printer,
            paper_size=self.paper_cb.currentText(),
            orientation=self.orientation_cb.currentText().lower(),
            color=self.color_cb.isChecked(),
            duplex=self.duplex_cb.currentText().lower(),
            page_range=(
                (self._os_from, self._os_to)
                if (self._os_from or self._os_to)
                else None
            ),
        )
        return pr

    def openDialog(self):
        if self.exec() != QDialog.Accepted:
            print("User cancelled the action")
            return

        print("User has accepted the action")
