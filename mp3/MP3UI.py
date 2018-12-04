# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Documents and Settings\Administrator\桌面\mp3\MP3.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 54, 12))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 220, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 220, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(100, 20, 256, 192))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.Umu)
        self.pushButton_2.clicked.connect(Dialog.Playmu)
        self.pushButton_3.clicked.connect(Dialog.Dmu)
        #self.queryBtn.clicked.connect(Form.queryWeather)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "播放列表"))
        self.pushButton.setText(_translate("Dialog", "上一首"))
        self.pushButton_2.setText(_translate("Dialog", "播放"))
        self.pushButton_3.setText(_translate("Dialog", "下一首"))




