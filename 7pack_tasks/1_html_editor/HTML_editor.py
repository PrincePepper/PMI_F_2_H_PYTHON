# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HTML_editor.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 681, 391))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.input.setObjectName("input")
        self.horizontalLayout.addWidget(self.input)
        self.output = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.output.setObjectName("output")
        self.horizontalLayout.addWidget(self.output)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 5, 681, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_input = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_input.setObjectName("label_input")
        self.horizontalLayout_2.addWidget(self.label_input)
        self.label_output = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_output.setObjectName("label_output")
        self.horizontalLayout_2.addWidget(self.label_output)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 440, 91, 27))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.translate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HTML редактор"))
        self.label_input.setText(_translate("MainWindow", "Ввод"))
        self.label_output.setText(_translate("MainWindow", "Вывод"))
        self.pushButton.setText(_translate("MainWindow", "Перевести"))

    def translate(self):
        self.output.setText(self.input.toPlainText())
