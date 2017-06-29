# -*- coding: latin-1 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

#Created by samhamnam

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sort
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 242)
        MainWindow.setFixedHeight(242)
        MainWindow.setFixedWidth(311)
        MainWindow.setWindowIcon(QtGui.QIcon("Icon/sort.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tOutput.setGeometry(QtCore.QRect(0, 180, 311, 61))
        self.tOutput.setObjectName("tOutput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 160, 47, 13))
        self.label.setObjectName("label")
        self.tSourceFolder = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tSourceFolder.setGeometry(QtCore.QRect(0, 20, 261, 21))
        self.tSourceFolder.setObjectName("tSourceFolder")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 131, 16))
        self.label_2.setObjectName("label_2")
        self.tOutputFolder = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tOutputFolder.setGeometry(QtCore.QRect(0, 70, 261, 21))
        self.tOutputFolder.setObjectName("tOutputFolder")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.label_3.setObjectName("label_3")
        self.bOutputButton = QtWidgets.QPushButton(self.centralwidget)
        self.bOutputButton.setGeometry(QtCore.QRect(260, 70, 51, 23))
        self.bOutputButton.setObjectName("bOutputButton")
        self.bSourceButton = QtWidgets.QPushButton(self.centralwidget)
        self.bSourceButton.setGeometry(QtCore.QRect(260, 20, 51, 23))
        self.bSourceButton.setObjectName("bSourceButton")
        self.bStart = QtWidgets.QPushButton(self.centralwidget)
        self.bStart.setGeometry(QtCore.QRect(10, 100, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bStart.setFont(font)
        self.bStart.setObjectName("bStart")
        MainWindow.setCentralWidget(self.centralwidget)

        self.tOutputFolder.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tSourceFolder.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tOutput.setPlainText("Warning the program might freeze during runtime! Just let it run and it will finish!\n Made by samhamnam\n")

        self.bOutputButton.clicked.connect(self.output_open)
        self.bSourceButton.clicked.connect(self.source_open)
        self.bStart.clicked.connect(self.start)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Sort", "Sort"))
        self.label.setText(_translate("MainWindow", "Output: "))
        self.label_2.setText(_translate("MainWindow", "Folder containing files: "))
        self.label_3.setText(_translate("MainWindow", "Output folder:"))
        self.bOutputButton.setText(_translate("MainWindow", "Browse"))
        self.bSourceButton.setText(_translate("MainWindow", "Browse"))
        self.bStart.setText(_translate("MainWindow", "Start"))

    def output_open(self):
        temp = QtWidgets.QFileDialog.getExistingDirectory()
        self.tOutputFolder.setPlainText(temp)
        self.tOutput.appendPlainText("Set output directory to: "+temp+"\n")

    def source_open(self):
        temp = QtWidgets.QFileDialog.getExistingDirectory()
        self.tSourceFolder.setPlainText(temp)
        self.tOutput.appendPlainText("Set source directory to: "+temp+"\n")

    def start(self):
        if self.tOutputFolder.toPlainText() != self.tSourceFolder.toPlainText():
            if os.path.isdir(self.tOutputFolder.toPlainText()) == True:
                if os.path.isdir(self.tSourceFolder.toPlainText()) == True:
                    sort.start(self.tSourceFolder.toPlainText(),self.tOutputFolder.toPlainText())
                    self.tOutput.appendPlainText("Starting!\n")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())