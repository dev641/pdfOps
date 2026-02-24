# backend/service.py
import shutil, subprocess, time
from dataclasses import dataclass
from typing import Optional, Tuple
from common.models.print.print_setting_dto import PrinterSettingsDTO
from common.models.print.print_result import PrintResult
from PySide6.QtCore import QObject


class PrintService(QObject):
    """
    Business logic for printing one file. Tries Ghostscript if available; falls back to simulated print.
    """

    def __init__(self, gs_path: Optional[str] = None):
        super().__init__()

        self.gs = (
            gs_path or shutil.which("gswin64c") or shutil.which("gswin32c")
        )

    def gs_available(self) -> bool:
        return bool(self.gs)

    def print_with_ghostscript(
        self, pdf_path: str, settings: PrinterSettingsDTO
    ) -> PrintResult:
        if not self.gs:
            return PrintResult(False, "", "Ghostscript not found")
        cmd = [
            self.gs,
            "-dNOPAUSE",
            "-dBATCH",
            "-sDEVICE=mswinpr2",
            f"-sOutputFile=%printer%{settings.printer_name}",
            f"-sPAPERSIZE={settings.paper_size}",
            "-dPDFFitPage",
        ]
        if not settings.color:
            cmd += ["-sColorConversionStrategy=Gray"]
        if settings.page_range:
            fr, to = settings.page_range
            if fr:
                cmd.append(f"-dFirstPage={fr}")
            if to:
                cmd.append(f"-dLastPage={to}")
        if settings.orientation == "landscape":
            cmd += ["-c", "<</Orientation 3>> setpagedevice"]
        if settings.duplex in ("long-edge", "short-edge"):
            tumble = "false" if settings.duplex == "long-edge" else "true"
            cmd += ["-c", f"<</Duplex true /Tumble {tumble}>> setpagedevice"]
        cmd += ["-f", pdf_path]
        try:
            proc = subprocess.run(
                cmd, capture_output=True, text=True, timeout=120
            )
            return PrintResult(
                proc.returncode == 0, proc.stdout or "", proc.stderr or ""
            )
        except subprocess.TimeoutExpired:
            return PrintResult(False, "", "Timeout")
        except Exception as e:
            return PrintResult(False, "", str(e))

    def mock_print(
        self, pdf_path: str, settings: PrinterSettingsDTO
    ) -> PrintResult:
        # Simulated printing: sleep briefly and return success — helpful for development/test without GS
        time.sleep(1.0)
        return PrintResult(ok=True, stdout="mock", stderr="")

    def print_one(
        self, pdf_path: str, settings: PrinterSettingsDTO
    ) -> PrintResult:
        return self.mock_print(pdf_path, settings)
        # if self.gs_available():
        #     return self.print_with_ghostscript(pdf_path, settings)
        # else:
        #     # No Ghostscript: do a mock print so UI flow can be tested
        #     return self.mock_print(pdf_path, settings)
