# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogWidget(object):
    def setupUi(self, LogWidget):
        LogWidget.setObjectName("LogWidget")
        LogWidget.setWindowModality(QtCore.Qt.WindowModal)
        LogWidget.resize(700, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LogWidget.sizePolicy().hasHeightForWidth())
        LogWidget.setSizePolicy(sizePolicy)
        LogWidget.setMinimumSize(QtCore.QSize(700, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("TWTools.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LogWidget.setWindowIcon(icon)
        LogWidget.setAutoFillBackground(True)
        self.gridLayout = QtWidgets.QGridLayout(LogWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.logText = QtWidgets.QPlainTextEdit(LogWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logText.sizePolicy().hasHeightForWidth())
        self.logText.setSizePolicy(sizePolicy)
        self.logText.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.logText.setReadOnly(True)
        self.logText.setPlainText("")
        self.logText.setCenterOnScroll(False)
        self.logText.setObjectName("logText")
        self.gridLayout.addWidget(self.logText, 0, 0, 1, 1)

        self.retranslateUi(LogWidget)
        QtCore.QMetaObject.connectSlotsByName(LogWidget)

    def retranslateUi(self, LogWidget):
        _translate = QtCore.QCoreApplication.translate
        LogWidget.setWindowTitle(_translate("LogWidget", "日志"))
