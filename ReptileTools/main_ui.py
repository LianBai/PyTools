# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(200, 100)
        MainWidget.setMinimumSize(QtCore.QSize(200, 100))
        MainWidget.setMaximumSize(QtCore.QSize(200, 100))
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DJDHBtn = QtWidgets.QPushButton(MainWidget)
        self.DJDHBtn.setMinimumSize(QtCore.QSize(80, 80))
        self.DJDHBtn.setObjectName("DJDHBtn")
        self.horizontalLayout.addWidget(self.DJDHBtn)
        self.SSSQBtn = QtWidgets.QPushButton(MainWidget)
        self.SSSQBtn.setMinimumSize(QtCore.QSize(80, 80))
        self.SSSQBtn.setObjectName("SSSQBtn")
        self.horizontalLayout.addWidget(self.SSSQBtn)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "抓包工具"))
        self.DJDHBtn.setText(_translate("MainWidget", "抓取\n"
"大江大河"))
        self.SSSQBtn.setText(_translate("MainWidget", "抓取\n"
"实时水情"))
