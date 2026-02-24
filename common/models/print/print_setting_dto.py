from ..model import Modal
from typing import Optional, Tuple


class PrinterSettingsDTO(Modal):
    printer_name: str
    paper_size: str = "a4"
    orientation: str = "portrait"
    color: bool = True
    duplex: str = "none"
    page_range: Optional[Tuple[Optional[int], Optional[int]]] = None
