from .model import Modal
from typing import Optional, Tuple


class PrinterSettings(Modal):
    printer_name: str
    paper_size: str = "a4"
    orientation: str = "portrait"  # "portrait"|"landscape"
    color: bool = True
    duplex: str = "none"  # "none"|"long-edge"|"short-edge"
    page_range: Optional[Tuple[Optional[int], Optional[int]]] = None

    class Config:
        validate_assignment = True
