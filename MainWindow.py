from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from forms.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.buttonSourceFolder.clicked.connect(self.setSourceFolder)
        self.buttonDestFolder.clicked.connect(self.setDestFolder)

    def setSourceFolder(self):
        self.lineEditSourceFolder.setText(self.getSelectedFolder())
        
    def setDestFolder(self):
        self.lineEditDestFolder.setText(self.getSelectedFolder())

    def getSelectedFolder(self):
        return QFileDialog.getExistingDirectory(self, "Select directory")

