# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(553, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    

        self.Boxes = []
        for i in range(8):
            self.Boxes.append(QtGui.QLabel(self.centralwidget))


        for i in range(4):
            self.Boxes[i].setGeometry(QtCore.QRect(60+i*120, 80 , 100, 100))
            self.Boxes[i].setAlignment(QtCore.Qt.AlignCenter)
            self.Boxes[i].setObjectName(_fromUtf8("Box" + str(i+1)))
            self.Boxes[i].setStyleSheet("QLabel{background-color : white;}")

        for i in range(4):
            self.Boxes[i+4].setGeometry(QtCore.QRect(60+i*120, 220 , 100, 100))
            self.Boxes[i+4].setAlignment(QtCore.Qt.AlignCenter)
            self.Boxes[i+4].setObjectName(_fromUtf8("Box" + str(i+5)))
            self.Boxes[i+4].setStyleSheet("QLabel{background-color : white;}")

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 420, 97, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))


        self.quantity = QtGui.QLabel(self.centralwidget)
        self.quantity.setGeometry(QtCore.QRect(70, 350, 201, 41))
        self.quantity.setStyleSheet(_fromUtf8(""))
        self.quantity.setAlignment(QtCore.Qt.AlignCenter)
        self.quantity.setObjectName(_fromUtf8("quantity"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(16, 30, 311, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "next", None))
        for i in range(8):
            self.Boxes[i].setText(_translate("MainWindow", "Box"+str(i+1), None))
        self.quantity.setText(_translate("MainWindow", "Quantity to be Picked", None))
        self.label.setText(_translate("MainWindow", "Status", None))

