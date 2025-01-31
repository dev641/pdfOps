from ..Layouts.layout_widget import VerticalLayoutWidget
from frontend.components.FileSelector.main import DragDropFileSelection
from .page import Page


class DragDropFilePage(Page):
    def __init__(self, pageId: str = "", pageTitle: str = ""):
        super().__init__(pageId=pageId, pageTitle=pageTitle)
        self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        self.layout.setSpacing(0)  # Remove spacing between widgets
        self.widget = DragDropFileSelection()
        self.addWidget(self.widget)
        self.setLayout(self.layout)
