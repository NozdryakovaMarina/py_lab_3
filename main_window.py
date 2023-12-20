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

import task1
import task2
import task3
from task5 import Iterator


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
        self.but1.setIcon(QIcon('folderm.svg'))
        self.but1.setFixedSize(QSize(540, 80))
        self.but1.clicked.connect(self.get_dir)
 
        self.but2 = QPushButton('CSV-Dataset', self)
        self.but2.setStyleSheet('background: #b0c4b1;color: #ffffff')
        self.but2.setIcon(QIcon('file_csv.svg'))
        self.but2.setFixedSize(QSize(540, 80))
        self.but2.clicked.connect(self.make_csv1)
 
        self.but3 = QPushButton('Copy dataset', self)
        self.but3.setStyleSheet('background: #b0c4b1;color: #ffffff')
        self.but3.setIcon(QIcon('folder.svg'))
        self.but3.setFixedSize(QSize(540, 80))
        self.but3.clicked.connect(self.get_change)
 
        self.but4 = QPushButton('Random dataset and create annotation', self)
        self.but4.setStyleSheet('background: #b0c4b1;color: #ffffff')
        self.but4.setIcon(QIcon('refresh.svg'))
        self.but4.setFixedSize(QSize(540, 80))
        self.but4.clicked.connect(self.get_copy)
 
        self.but5 = QPushButton('Next Polar Bear', self)
        self.but5.setIcon(QIcon('sr.svg'))
        self.but5.setFixedSize(QSize(540, 80))
        self.but5.setStyleSheet('background: #4a5759; color: #ffffff')
        self.but5.clicked.connect(self.next_polar)
 
        self.but6 = QPushButton('Next Brown Bear', self)
        self.but6.setIcon(QIcon('sr.svg'))
        self.but6.setFixedSize(QSize(540, 80))
        self.but6.setStyleSheet('background: #4a5759; color: #ffffff')
        self.but6.clicked.connect(self.next_brown)

        self.but7 = QPushButton('CSV-Dataset2', self)
        self.but7.setStyleSheet('background: #4a5759;color: #ffffff')
        self.but7.setIcon(QIcon('file_csv.svg'))
        self.but7.setFixedSize(QSize(540, 80))
        self.but7.clicked.connect(self.make_csv2)

        self.but8 = QPushButton('Application Programming', self)
        self.but8.setStyleSheet('background: #b0c4b1;color: #ffffff')
        self.but8.setFixedSize(QSize(540, 80))

        self.but9 = QPushButton('Laboratory Work', self)
        self.but9.setStyleSheet('background: #b0c4b1;color: #ffffff')
        self.but9.setFixedSize(QSize(540, 80))

        self.but10 = QPushButton('GUI', self)
        self.but10.setStyleSheet('background: #b0c4b1;color: #ffffff') 
        self.but10.setFixedSize(QSize(540, 80)) 

        self.but11 = QPushButton('Option 5', self)
        self.but11.setStyleSheet('background: #b0c4b1;color: #ffffff') 
        self.but11.setFixedSize(QSize(540, 80)) 

        self.label = QLabel(self)
         
        gridL = QGridLayout()
        gridL.setSpacing(5)
        
        gridL.addWidget(self.but1, 0, 3)
        gridL.addWidget(self.but2, 1, 3)
        gridL.addWidget(self.but3, 2, 3)
        gridL.addWidget(self.but4, 3, 3)
        gridL.addWidget(self.but5, 4, 0)
        gridL.addWidget(self.but6, 4, 1)
        gridL.addWidget(self.but7, 4, 3)
        gridL.addWidget(self.but8, 0, 0)
        gridL.addWidget(self.but9, 1, 0)
        gridL.addWidget(self.but10, 2, 0)
        gridL.addWidget(self.but11, 3, 0)
        gridL.addWidget(self.label, 0, 1, 4, 1, alignment=Qt.AlignCenter)

        self.setLayout(gridL)

        self.showMaximized()
        self.show()

    
    def quit(self):
        if self.confirm_save():
            self.destroy() 

    def folder(self) -> str:
        """
        selecting a folder
        """
        dir_n = QFileDialog.getExistingDirectory(self, "Select folder")
        return dir_n

    def get_dir(self) -> None:
        """
        Getting the path to the dataset
        """
        self.dir_n = QFileDialog.getExistingDirectory(self, "Select Directory")
        path = self.folder()
        if os.path.exists(os.path.join(path, "polar_bear")) | os.path.exists(os.path.join(path, "brown_bear")):
            self.iter()
            self.mes("Nice")
        else:
            self.mes("The directory was not found")

    def make_csv1(self) -> None:
        """
        This function creates an annotation for the dataset
        """
        p = self.folder()
        if os.path.exists(os.path.join(p, "polar_bear")) & os.path.exists(
            os.path.join(p, "brown_bear")
        ):
            task1.create_csv('polar_bear', 'annotation.csv', 'dataset')
            task1.create_csv('brown_bear', 'annotation.csv', 'dataset')
            self.mes("Successfully!")
        else:
            self.mes("The folder is incorrectly selected")

    def make_csv2(self) -> None:
        """
        This function creates an annotation for the dataset
        """
        p = self.folder()
        if os.path.exists(os.path.join(p, "polar_bear")) & os.path.exists(
            os.path.join(p, "brown_bear")
        ):
            task2.create_csv2('polar_bear', 'annotation.csv', 'dataset')
            task2.create_csv2('brown_bear', 'annotation.csv', 'dataset')
            self.mes("Successfully!")
        else:
            self.mes("The folder is incorrectly selected")

    def get_change(self) -> None:
        """
        Copies dataset to dataset2 with new names and creates a csv file
        """

        p = self.folder()
        if os.path.exists(os.path.join(p, "polar_bear")) & os.path.exists(
            os.path.join(p, "brown_bear")
        ):
            task2.change('dataset', 'dataset2', ['polarbear', 'brownbear'])
            self.mes("Successfully!")
        else:
            self.mes("The folder is incorrectly selected")


    def get_copy(self) -> None:
        """
        Copies dataset to dataset3 with random names and creates a csv file.
        """

        p = self.folder()
        if os.path.exists(os.path.join(p, "polar_bear")) & os.path.exists(
            os.path.join(p, "brown_bear")
        ):
            task3.copy('dataset', 'dataset3')
            self.mes("Successfully!")
        else:
            self.mes("The folder is incorrectly selected")

    def iter(self) -> None:
        """
        This function creates two iterator objects for displaying images
        """
        self.polarbear1 = Iterator('polar_bear', self.dir_n)
        self.brownbear1 = Iterator('brown_bear', self.dir_n)

    def next_polar(self) -> None:
        """
        This function gets the next instance of the image and places it on the main window
        """

        p_p = next(self.polarbear1)
        if p_p != None:
            image = QPixmap(p_p)
            image_rez = image.scaledToHeight(340)
            self.label.setPixmap(image_rez)
        else:
            self.mes("End")
            self.iter()
            self.next_polar()

    def next_brown(self) -> None:
        """
        This function gets the next instance of the image and places it on the main window
        """
        b_p = next(self.brownbear1)
        if b_p != None:
            image = QPixmap(b_p)
            image_rez = image.scaledToHeight(340)
            self.label.setPixmap(image_rez)
        else:
            self.mes("End")
            self.iter()
            self.next_brown()

    def mes(self, text: str) -> None:
        """
        """
        d = QDialog(self)
        d.setWindowTitle("BEAR")
        text = QLabel(text, d)
        but = QPushButton("OK", d)
        vbox = QVBoxLayout(d)
        vbox.addStretch(1)
        vbox.addWidget(text)
        vbox.addWidget(but)
        but.clicked.connect(d.close)
        d.exec()


def main() -> None:
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()