from ..Layouts.layout_widget import VerticalLayoutWidget
from frontend.components.Labels.label import LabeledText
from PySide6.QtWidgets import QWidget


class Page(VerticalLayoutWidget):
    def __init__(self, pageId: str, pageTitle: str):
        super().__init__()
        self._pageId = pageId
        self._pageTitle = pageTitle

    @property
    def pageId(self):
        return self._pageId

    @pageId.setter
    def pageId(self, value):
        self._pageId = value

    @property
    def pageTitle(self):
        return self._pageTitle

    @pageTitle.setter
    def pageTitle(self, value):
        self._pageTitle = value

    def to_dict(self):
        return {
            "pageId": self._pageId,
            "pageTitle": self._pageTitle,
        }

    def __len___(self):
        return len(self.to_dict())

    def __repr__(self):
        return (
            super().__repr__() + f"Page('{self._pageId}', '{self._pageTitle}')"
        )

    def __str__(self):
        return (
            super().__str__() + f"Page('{self._pageId}', '{self._pageTitle}')"
        )
