from ..model import Modal


class PrintResult(Modal):
    ok: bool
    stdout: str = ""
    stderr: str = ""
