# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ksusha\PycharmProjects\Графика1\ShamirWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShamirWind(object):
    def setupUi(self, ShamirWind):
        ShamirWind.setObjectName("ShamirWind")
        ShamirWind.resize(1048, 916)
        ShamirWind.setMinimumSize(QtCore.QSize(0, 0))
        ShamirWind.setMaximumSize(QtCore.QSize(4564756, 16777215))
        ShamirWind.setLayoutDirection(QtCore.Qt.LeftToRight)
        ShamirWind.setGeometry(500, 60, 1000, 800)
        self.centralwidget = QtWidgets.QWidget(ShamirWind)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 19, 3, 1, 2)
        self.x1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.x1.setReadOnly(True)
        self.x1.setObjectName("x1")
        self.gridLayout.addWidget(self.x1, 13, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 11, 0, 1, 4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 11, 4, 1, 1)
        self.x2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.x2.setReadOnly(True)
        self.x2.setObjectName("x2")
        self.gridLayout.addWidget(self.x2, 13, 4, 1, 1)
        self.x3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.x3.setReadOnly(True)
        self.x3.setObjectName("x3")
        self.gridLayout.addWidget(self.x3, 15, 1, 1, 1)
        self.da = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.da.setReadOnly(False)
        self.da.setObjectName("da")
        self.gridLayout.addWidget(self.da, 6, 1, 1, 1)
        self.Ca = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Ca.setReadOnly(False)
        self.Ca.setObjectName("Ca")
        self.gridLayout.addWidget(self.Ca, 3, 1, 1, 1)
        self.db = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.db.setReadOnly(False)
        self.db.setObjectName("db")
        self.gridLayout.addWidget(self.db, 6, 4, 1, 1)
        self.Cb = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Cb.setReadOnly(False)
        self.Cb.setObjectName("Cb")
        self.gridLayout.addWidget(self.Cb, 3, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 5)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 15, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 15, 2, 1, 1)
        self.x4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.x4.setReadOnly(True)
        self.x4.setObjectName("x4")
        self.gridLayout.addWidget(self.x4, 15, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 12, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 2, 1, 1)
        self.mi = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.mi.setReadOnly(True)
        self.mi.setObjectName("mi")
        self.gridLayout.addWidget(self.mi, 12, 1, 1, 4)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 19, 0, 1, 3)
        self.p = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.p.setObjectName("p")
        self.gridLayout.addWidget(self.p, 0, 1, 2, 3)
        self.m = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.m.setReadOnly(False)
        self.m.setObjectName("m")
        self.gridLayout.addWidget(self.m, 10, 0, 1, 5)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 13, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 13, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 17, 0, 1, 5)
        self.plainTextEdit_13 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_13.setReadOnly(True)
        self.plainTextEdit_13.setObjectName("plainTextEdit_13")
        self.gridLayout.addWidget(self.plainTextEdit_13, 18, 0, 1, 5)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 20, 0, 1, 5)
        ShamirWind.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ShamirWind)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 26))
        self.menubar.setObjectName("menubar")
        ShamirWind.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ShamirWind)
        self.statusbar.setObjectName("statusbar")
        ShamirWind.setStatusBar(self.statusbar)

        self.retranslateUi(ShamirWind)
        QtCore.QMetaObject.connectSlotsByName(ShamirWind)

    def retranslateUi(self, ShamirWind):
        _translate = QtCore.QCoreApplication.translate
        ShamirWind.setWindowTitle(_translate("ShamirWind", "КМЗИ"))
        self.label_2.setText(_translate("ShamirWind", "da:"))
        self.label_4.setText(_translate("ShamirWind", "Cb:"))
        self.pushButton_8.setText(_translate("ShamirWind", "Очистить перед передачей нового сообщения"))
        self.pushButton_4.setText(_translate("ShamirWind", "Отправить поэтапно"))
        self.pushButton_5.setText(_translate("ShamirWind", "Отправить целиком"))
        self.pushButton_3.setText(_translate("ShamirWind", "Найти da и db:"))
        self.label_11.setText(_translate("ShamirWind", "x3:"))
        self.label.setText(_translate("ShamirWind", "Простое число p = "))
        self.label_10.setText(_translate("ShamirWind", "x4:"))
        self.label_7.setText(_translate("ShamirWind", "mi ="))
        self.label_5.setText(_translate("ShamirWind", "Введите сообщение для отправления:"))
        self.pushButton.setText(_translate("ShamirWind", "Сгенерировать параметры"))
        self.label_6.setText(_translate("ShamirWind", "db:"))
        self.pushButton_6.setText(_translate("ShamirWind", "Передать файл"))
        self.label_8.setText(_translate("ShamirWind", "x1:"))
        self.pushButton_2.setText(_translate("ShamirWind", "Проверить на простоту"))
        self.label_9.setText(_translate("ShamirWind", "x2:"))
        self.label_3.setText(_translate("ShamirWind", "Ca:"))
        self.label_12.setText(_translate("ShamirWind", "Полученное сообщение:"))
        self.pushButton_7.setText(_translate("ShamirWind", "Очистить"))