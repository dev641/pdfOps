from frontend.components.ComboBox.comboBox import ComboBox
from frontend.components.Dialog.dialog_button_box import DialogButtonBox
from frontend.container.Layouts.layout_widget import VerticalDialogWidget


class ComboBoxDialog(VerticalDialogWidget):

    def __init__(
        self, title, dropDownOptions, onItemSelected=None, parent=None
    ):
        super().__init__()
        self.setWindowTitle(title)
        self.setModal(True)
        # self.setFixedSize(600, 200)
        # Add a ComboBox with options
        self.comboBox = ComboBox(
            items=dropDownOptions,
            parent=self,
            onItemSelected=onItemSelected,
            # width=600,
            # height=200,
        )

        self.addWidget(self.comboBox)
        self.addDialogButtonBox()
        self.setLayout(self.layout)

    def addDialogButtonBox(self):
        buttonBox = DialogButtonBox(parent=self)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        self.addWidget(buttonBox)

    def getSelectedOption(self):
        """Return the selected option when dialog is accepted."""
        if self.exec() == VerticalDialogWidget.Accepted:
            return self.comboBox.currentText()
        return None
