# -*- coding: latin-1 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *  # noqa: F403, F401
from PyQt5.QtGui import *  # noqa: F403, F401
import os
import shutil
import webbrowser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.move_mode = True
        self.abc_mode = False
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 242)
        MainWindow.setFixedHeight(257)  # 240
        MainWindow.setFixedWidth(311)
        MainWindow.setWindowIcon(QtGui.QIcon("Icon/sort.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tOutput.setGeometry(QtCore.QRect(0, 180, 311, 61))
        self.tOutput.setObjectName("tOutput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 165, 47, 13))
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
        self.tOutput.setReadOnly(True)

        self.bCopy_Move = QtWidgets.QCheckBox(self.centralwidget)
        self.bCopy_Move.setGeometry(QtCore.QRect(132, 237, 128, 23))
        self.bCopy_Move.setObjectName("Check")
        self.bCopy_Move.setText("Copy instead of move")
        self.bCopy_Move.clicked.connect(self.Copy_Move)
        self.bCopy_Move.setDisabled(True)

        self.bABC_Move = QtWidgets.QCheckBox(self.centralwidget)
        self.bABC_Move.setGeometry(QtCore.QRect(2, 237, 128, 23))
        self.bABC_Move.setObjectName("ABC")
        self.bABC_Move.clicked.connect(self.dAbc_mode)
        self.bABC_Move.setText("Sort by letters instead")

        self.bSourceCode = QtWidgets.QPushButton(self.centralwidget)
        self.bSourceCode.setGeometry(QtCore.QRect(260, 240, 51, 18))
        self.bSourceCode.setObjectName("bSourceCode")
        self.bSourceCode.setText("Source")
        self.bSourceCode.clicked.connect(self.open_source)

        self.tOutputFolder.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.tSourceFolder.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.tOutput.setPlainText(
            "Warning the program might freeze during runtime!" +
            "Just let it run and it will finish!" +
            "\nMake sure output folder is empty!" +
            "\nMade by samhamnam. Idea from Emalphi"
        )

        self.bOutputButton.clicked.connect(self.output_open)
        self.bSourceButton.clicked.connect(self.source_open)
        self.bStart.clicked.connect(self.start)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Sort", "Sort"))
        self.label.setText(_translate("MainWindow", "Output: "))
        self.label_2.setText(_translate(
            "MainWindow",
            "Folder containing files: ")
        )
        self.label_3.setText(_translate("MainWindow", "Output folder:"))
        self.bOutputButton.setText(_translate("MainWindow", "Browse"))
        self.bSourceButton.setText(_translate("MainWindow", "Browse"))
        self.bStart.setText(_translate("MainWindow", "Start"))

    def output_open(self):
        temp = QtWidgets.QFileDialog.getExistingDirectory()
        self.tOutputFolder.setPlainText(temp)
        self.tOutput.appendPlainText("Set output directory to: "+temp)
        self.tOutput.moveCursor(QtGui.QTextCursor.End)

    def source_open(self):
        temp = QtWidgets.QFileDialog.getExistingDirectory()
        self.tSourceFolder.setPlainText(temp)
        self.tOutput.appendPlainText("Set source directory to: "+temp)
        self.tOutput.moveCursor(QtGui.QTextCursor.End)

    def start(self):
        if self.tOutputFolder.toPlainText() != self.tSourceFolder.toPlainText():  # noqa: E501
            if os.path.isdir(self.tOutputFolder.toPlainText()) is True:
                if os.path.isdir(self.tSourceFolder.toPlainText()) is True:
                    self.tOutput.appendPlainText("Starting!")
                    self.start_sort(
                        self.tSourceFolder.toPlainText(),
                        self.tOutputFolder.toPlainText()
                    )
                    self.tOutput.moveCursor(QtGui.QTextCursor.End)

    def start_sort(self, working_dir, sorted_dir):
        if os.path.isdir(working_dir) is True:
            self.tOutput.appendPlainText("Found directory: "+working_dir)
            self.tOutput.moveCursor(QtGui.QTextCursor.End)
        else:
            self.tOutput.appendPlainText("This aint no directory!")
            self.tOutput.moveCursor(QtGui.QTextCursor.End)

        if os.path.isdir(sorted_dir) is True:
            self.tOutput.appendPlainText("Found directory: "+str(sorted_dir))
            self.tOutput.moveCursor(QtGui.QTextCursor.End)
        else:
            self.tOutput.appendPlainText("This aint no directory!")
            self.tOutput.moveCursor(QtGui.QTextCursor.End)

        if os.path.isdir(sorted_dir) is False:
            os.mkdir(sorted_dir)

        try:
            self.bStart.setDisabled(True)
            for file in os.listdir(working_dir):
                if file.endswith(""):
                    self.tOutput.moveCursor(QtGui.QTextCursor.End)
                    filename, file_extension = os.path.splitext(file)
                    filename = filename  # Just outsmarting pylint :P
                    if self.abc_mode is False:
                        if os.path.isdir(sorted_dir+"/"+file_extension) is False:  # noqa: E501
                            if len(file_extension) > 0:
                                self.tOutput.appendPlainText(
                                    "Created directory: "+file_extension
                                )
                                self.tOutput.moveCursor(QtGui.QTextCursor.End)
                                os.mkdir(sorted_dir+"/"+file_extension)
                    else:
                        if os.path.isdir(sorted_dir+"/"+file[:1]) is False:
                            if len(file_extension) > 0:
                                self.tOutput.appendPlainText(
                                    "Created directory: "+file[:1]
                                )
                                self.tOutput.moveCursor(QtGui.QTextCursor.End)
                                os.mkdir(sorted_dir+"/"+file[:1])

                    if self.abc_mode is False:
                        if self.move_mode is True:
                            shutil.move(
                                working_dir+"/"+file,
                                sorted_dir+"/"+file_extension
                            )
                        if self.move_mode is False:
                            if os.path.isdir(working_dir+"/"+file):
                                shutil.copytree(
                                    working_dir+"/"+file,
                                    sorted_dir+"/"+file_extension+file
                                )
                            else:
                                shutil.copytree(
                                    working_dir+"/"+file,
                                    sorted_dir+"/"+file_extension+"/"+file
                                )
                    else:
                        if self.move_mode is True:
                            shutil.move(
                                working_dir+"/"+file,
                                sorted_dir+"/"+file[:1]+"/"+file
                            )
                        if self.move_mode is False:
                            if os.path.isdir(working_dir+"/"+file):
                                shutil.copytree(
                                    working_dir+"/"+file,
                                    sorted_dir+"/"+file[:1]+"/"
                                )
                            else:
                                shutil.copytree(
                                    working_dir+"/"+file,
                                    sorted_dir+"/"+file[:1]+"/"
                                )

        finally:
            self.tOutput.appendPlainText(
                "Done! If it didn't work please contact samhamnam!")
            self.bStart.setDisabled(False)

    def open_source(self):
        webbrowser.open("https://bitbucket.org/samhamnam/sort/overview")

    def Copy_Move(self):
        if self.bCopy_Move.isChecked() is True:
            self.move_mode = True
            print(self.move_mode)
        else:
            self.move_mode = False
            print(self.move_mode)

    def dAbc_mode(self):
        if self.bABC_Move.isChecked() is True:
            self.abc_mode = True
            print(self.abc_mode)
        else:
            self.abc_mode = False
            print(self.abc_mode)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
