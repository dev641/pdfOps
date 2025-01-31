import sys
from PySide6.QtWidgets import (
    QApplication,
)
from frontend.container.window import MainWindow

# from common.utils.debug_layout_structure import debug_layout


def main():
    app = QApplication(sys.argv)  # Create the application
    window = MainWindow()  # Create the window
    # debug_layout(window)
    window.show()  # Show the window
    sys.exit(app.exec())  # Start the application event loop


if __name__ == "__main__":
    main()
