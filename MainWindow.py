from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(QMainWindow, self).__init__(parent)

        self.sourceFolder = QtWidgets.QLineEdit(self)
        self.chooseSourceFolder = QtWidgets.QPushButton(self)
        self.chooseSourceFolder.setText("..")
        self.destinationFolder = QtWidgets.QLineEdit(self)
        self.chooseDestinationFolder = QtWidgets.QPushButton(self)
        self.chooseDestinationFolder.setText("..")
        self.listView = QtWidgets.QListView(self)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.addWidget(self.sourceFolder, 0, 0, 1, 8)
        self.gridLayout.addWidget(self.chooseSourceFolder, 0, 8, 1, 1)
        self.gridLayout.addWidget(self.destinationFolder, 1, 0, 1, 8)
        self.gridLayout.addWidget(self.chooseDestinationFolder, 1, 8, 1, 1)
        self.gridLayout.addWidget(self.listView, 2, 0, 6, 9)
        
        self.main_widget = QtWidgets.QWidget(self)
        self.main_widget.setLayout(self.gridLayout)
        self.setCentralWidget(self.main_widget)
