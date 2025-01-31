from .model import Modal


class Data(Modal):
    def __init__(self, pdf_name: str, page_count: int):
        super().__init__()
        self._pdf_name = (
            pdf_name  # Use a private variable for storing the pdf name
        )
        self._page_count = (
            page_count  # Use a private variable for storing the page count
        )

    def to_dict(self):
        return {
            "pdf_name": self.pdf_name,
            "page_count": self.page_count,
        }

    def __str__(self):
        return f"Data: (pdf name={self.pdf_name}, page={self.page_count})"

    def __repr__(self):
        return f"Data: (pdf name={self.pdf_name}, page={self.page_count})"

    @property
    def pdf_name(self):
        return self._pdf_name  # Access the private variable

    @pdf_name.setter
    def pdf_name(self, value):
        self._pdf_name = value  # Set the private variable

    @property
    def page_count(self):
        return self._page_count  # Access the private variable

    @page_count.setter
    def page_count(self, value):
        self._page_count = value  # Set the private variable
