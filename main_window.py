import os
import sys
from typing import List

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QEvent, QSize
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QGridLayout,
    QPushButton,
    QVBoxLayout,
    QWidget
)
from PyQt5.QtWidgets import *

from task5 import Iterator

import task1
import task2
import task3


class MainWindow(QWidget):
    def __init__(self):
        """
        This function calls the methods necessary to create a window
        """
        super().__init__()

        self.initUI()
        self.setStyleSheet(
            'background: #f7e1d7; color: #000000; font-weight:bold; border-radius: 5px; font-size: 20px;')

    def initUI(self) -> None:
        """
        This function creates the main widget and places the buttons according to the layout
        """
        self.setWindowTitle('POLAR&BROWN')
        self.setWindowIcon(QIcon('bear.svg'))
        self.setGeometry(200, 300, 200, 200) 

        self.but1 = QPushButton('Source dataset', self)
        self.but1.setStyleSheet('background: #b0c4b1;color: #ffffff')
        self.but1.setIcon(QIcon('img/folderm.png'))
        self.but1.setFixedSize(QSize(500, 80))
        self.but1.clicked.connect(self.get_dir)
 
        self.but2 = QPushButton('CSV-Dataset', self)
        self.but2.setStyleSheet('background: #b0c4b1;color: #ffffff')
        self.but2.setIcon(QIcon('img/file_csv.png'))
        self.but2.setFixedSize(QSize(500, 80))
        self.but2.clicked.connect(self.make_csv)
 
        self.but3 = QPushButton('Copy dataset and create annotation', self)
        self.but3.setStyleSheet('background: #b0c4b1;color: #ffffff')
        self.but3.setIcon(QIcon('img/folder.png'))
        self.but3.setFixedSize(QSize(500, 80))
        self.but3.clicked.connect(self.get_change)
 
        self.but4 = QPushButton('Random dataset and create annotation', self)
        self.but4.setStyleSheet('background: #b0c4b1;color: #ffffff')
        self.but4.setIcon(QIcon('img/refresh.png'))
        self.but4.setFixedSize(QSize(500, 80))
        self.but4.clicked.connect(self.get_copy)
 
        self.but5 = QPushButton('Next Polar Bear', self)
        self.but5.setIcon(QIcon('img/sr.png'))
        self.but5.setFixedSize(QSize(500, 80))
        self.but5.setStyleSheet('background: #4a5759; color: #ffffff')
 
        self.but6 = QPushButton('Next Brown Bear', self)
        self.but6.setIcon(QIcon('img/sr.png'))
        self.but6.setFixedSize(QSize(500, 80))
        self.but6.setStyleSheet('background: #4a5759; color: #ffffff')

        self.label = QLabel(self)

        gridL = QGridLayout()
        gridL.setSpacing(5)
        
        gridL.addWidget(self.but1, 0, 3)
        gridL.addWidget(self.but2, 1, 3)
        gridL.addWidget(self.but3, 2, 3)
        gridL.addWidget(self.but4, 3, 3)
        gridL.addWidget(self.but5, 4, 0)
        gridL.addWidget(self.but6, 4, 1)
        gridL.addWidget(self.label, 0, 1, 4, 1, alignment=Qt.AlignCenter)

        self.setLayout(gridL)

        self.showMaximized()
        self.show()

    def get_dir(self) -> None:
        """
        """
        res = QMessageBox.information(self, 'Information', "The directory was not found",
                                      QMessageBox.Ok | QMessageBox.Cancel)
        if res == QMessageBox.Ok:
            self.res.close()
        else:
            pass

    def make_csv(self) -> None:
        """
        This function creates an annotation for the dataset
        """
        res1 = QMessageBox.information(self, 'Information', "Successfully!",
                                      QMessageBox.Ok | QMessageBox.Cancel)
        if res1 == QMessageBox.Ok:
            self.res1.close()
        else:
            pass
        
        res2 = QMessageBox.warning(self, 'Information', "The folder is incorrectly selected",
                                      QMessageBox.Ok | QMessageBox.Cancel)
        if res2 == QMessageBox.Ok:
            self.res2.close()
        else:
            pass


    def get_change(self) -> None:
        """
        Copies dataset to dataset2 with new names and creates a csv file
        """
        res1 = QMessageBox.information(self, 'Information', "Successfully!",
                                      QMessageBox.Ok | QMessageBox.Cancel)
        if res1 == QMessageBox.Ok:
            self.res1.close()
        else:
            pass
        
        res2 = QMessageBox.warning(self, 'Information', "The folder is incorrectly selected",
                                      QMessageBox.Ok | QMessageBox.Cancel)
        if res2 == QMessageBox.Ok:
            self.res2.close()
        else:
            pass


    def get_copy(self) -> None:
        """
        Copies dataset to dataset3 with random names and creates a csv file.
        """
        res1 = QMessageBox.information(self, 'Information', "Successfully!",
                                      QMessageBox.Ok | QMessageBox.Cancel)
        if res1 == QMessageBox.Ok:
            self.res1.close()
        else:
            pass
        
        res2 = QMessageBox.warning(self, 'Information', "The folder is incorrectly selected",
                                      QMessageBox.Ok | QMessageBox.Cancel)
        if res2 == QMessageBox.Ok:
            self.res2.close()
        else:
            pass

    def iter(self) -> None:
        """
        This function creates two iterator objects for displaying images
        """
        self.polarbear1: Iterator = Iterator('polarbear', self.dir_name)
        self.brownbear1: Iterator = Iterator('brownbear', self.dir_name)

    def next_polar(self) -> None:
        """
        This function gets the next instance of the image and places it on the main window
        """
        res1 = QMessageBox.information(self, 'Information', "Successfully!",
                                      QMessageBox.Ok | QMessageBox.Cancel)
        if res1 == QMessageBox.Ok:
            self.res1.close()
        else:
            pass

    def next_brown(self) -> None:
        """
        This function gets the next instance of the image and places it on the main window
        """
        res1 = QMessageBox.information(self, 'Information', "Successfully!",
                                      QMessageBox.Ok | QMessageBox.Cancel)
        if res1 == QMessageBox.Ok:
            self.res1.close()
        else:
            pass


def main() -> None:
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()