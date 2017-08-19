# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Aug 19 22:19:58 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(426, 319)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditSourceFolder = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditSourceFolder.setObjectName("lineEditSourceFolder")
        self.gridLayout.addWidget(self.lineEditSourceFolder, 2, 3, 1, 1)
        self.buttonSourceFolder = QtWidgets.QPushButton(self.centralWidget)
        self.buttonSourceFolder.setMaximumSize(QtCore.QSize(30, 16777215))
        self.buttonSourceFolder.setObjectName("buttonSourceFolder")
        self.gridLayout.addWidget(self.buttonSourceFolder, 2, 4, 1, 1)
        self.lineEditDestFolder = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditDestFolder.setObjectName("lineEditDestFolder")
        self.gridLayout.addWidget(self.lineEditDestFolder, 5, 3, 1, 1)
        self.buttonDestFolder = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDestFolder.sizePolicy().hasHeightForWidth())
        self.buttonDestFolder.setSizePolicy(sizePolicy)
        self.buttonDestFolder.setMaximumSize(QtCore.QSize(30, 16777215))
        self.buttonDestFolder.setObjectName("buttonDestFolder")
        self.gridLayout.addWidget(self.buttonDestFolder, 5, 4, 1, 1)
        self.labelSourceFolder = QtWidgets.QLabel(self.centralWidget)
        self.labelSourceFolder.setObjectName("labelSourceFolder")
        self.gridLayout.addWidget(self.labelSourceFolder, 2, 2, 1, 1)
        self.labelDestFolder = QtWidgets.QLabel(self.centralWidget)
        self.labelDestFolder.setObjectName("labelDestFolder")
        self.gridLayout.addWidget(self.labelDestFolder, 5, 2, 1, 1)
        self.listViewBooks = QtWidgets.QListView(self.centralWidget)
        self.listViewBooks.setObjectName("listViewBooks")
        self.gridLayout.addWidget(self.listViewBooks, 7, 2, 1, 3)
        self.buttonStart = QtWidgets.QPushButton(self.centralWidget)
        self.buttonStart.setObjectName("buttonStart")
        self.gridLayout.addWidget(self.buttonStart, 0, 2, 1, 3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonSourceFolder.setText(_translate("MainWindow", "..."))
        self.buttonDestFolder.setText(_translate("MainWindow", "..."))
        self.labelSourceFolder.setText(_translate("MainWindow", "Source Folder"))
        self.labelDestFolder.setText(_translate("MainWindow", "Destination folder"))
        self.buttonStart.setText(_translate("MainWindow", "Start"))

