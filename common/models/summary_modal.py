from .model import Modal


class SummaryModal(Modal):
    def __init__(
        self, total_pages: int = 0, rate: float = 0.0, total_cost: float = 0.0
    ):
        super().__init__()
        self._total_pages = total_pages
        self._rate = rate
        self._total_cost = total_cost

    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value

    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, value):
        self._total_cost = value

    def to_dict(self):
        return {
            "total_pages": self.total_pages,
            "rate": self.rate,
            "total_cost": self.total_cost,
        }

    def __str__(self):
        return f"SummaryModal: (total_pages={self.total_pages}, rate={self.rate}, total_cost={self.total_cost})"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.to_dict())
