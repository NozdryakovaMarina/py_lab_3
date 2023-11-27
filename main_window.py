import sys

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
        self.menuBar()
        self.toolBar()
        self.statusBar()

    def init(self):
        self.setWindowTitle('~GUI&IMAGE~')
        self.setWindowIcon(QIcon('img/image.png'))
        self.setCentralWidget(QWidget())
        


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()