# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.setWindowModality(QtCore.Qt.WindowModal)
        MainWidget.setEnabled(True)
        MainWidget.resize(293, 118)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        MainWidget.setMinimumSize(QtCore.QSize(0, 0))
        MainWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWidget.setSizeIncrement(QtCore.QSize(0, 0))
        MainWidget.setBaseSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(MainWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.BlogLabel = QtWidgets.QLabel(MainWidget)
        self.BlogLabel.setObjectName("BlogLabel")
        self.gridLayout.addWidget(self.BlogLabel, 0, 0, 1, 1)
        self.BlogPath = QtWidgets.QLabel(MainWidget)
        self.BlogPath.setMinimumSize(QtCore.QSize(140, 40))
        self.BlogPath.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.BlogPath.setFont(font)
        self.BlogPath.setAutoFillBackground(False)
        self.BlogPath.setScaledContents(True)
        self.BlogPath.setAlignment(QtCore.Qt.AlignCenter)
        self.BlogPath.setWordWrap(True)
        self.BlogPath.setObjectName("BlogPath")
        self.gridLayout.addWidget(self.BlogPath, 0, 1, 1, 1)
        self.BlogPathSearchBtn = QtWidgets.QPushButton(MainWidget)
        self.BlogPathSearchBtn.setObjectName("BlogPathSearchBtn")
        self.gridLayout.addWidget(self.BlogPathSearchBtn, 0, 2, 1, 1)
        self.BtnsLayout = QtWidgets.QGridLayout()
        self.BtnsLayout.setObjectName("BtnsLayout")
        self.DeployBtn = QtWidgets.QPushButton(MainWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.DeployBtn.setFont(font)
        self.DeployBtn.setObjectName("DeployBtn")
        self.BtnsLayout.addWidget(self.DeployBtn, 0, 1, 1, 1)
        self.OpenPostPathBtn = QtWidgets.QPushButton(MainWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenPostPathBtn.setFont(font)
        self.OpenPostPathBtn.setObjectName("OpenPostPathBtn")
        self.BtnsLayout.addWidget(self.OpenPostPathBtn, 1, 1, 1, 1)
        self.OpenBlogPathBtn = QtWidgets.QPushButton(MainWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenBlogPathBtn.setFont(font)
        self.OpenBlogPathBtn.setObjectName("OpenBlogPathBtn")
        self.BtnsLayout.addWidget(self.OpenBlogPathBtn, 1, 0, 1, 1)
        self.DeployPushBtn = QtWidgets.QPushButton(MainWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.DeployPushBtn.setFont(font)
        self.DeployPushBtn.setObjectName("DeployPushBtn")
        self.BtnsLayout.addWidget(self.DeployPushBtn, 0, 2, 1, 1)
        self.DebugBtn = QtWidgets.QPushButton(MainWidget)
        self.DebugBtn.setEnabled(True)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.DebugBtn.setFont(font)
        self.DebugBtn.setObjectName("DebugBtn")
        self.BtnsLayout.addWidget(self.DebugBtn, 0, 0, 1, 1)
        self.CreatPostBtn = QtWidgets.QPushButton(MainWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.CreatPostBtn.setFont(font)
        self.CreatPostBtn.setObjectName("CreatPostBtn")
        self.BtnsLayout.addWidget(self.CreatPostBtn, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.BtnsLayout, 1, 0, 1, 3)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "博客工具"))
        self.BlogLabel.setText(_translate("MainWidget", "项目路径"))
        self.BlogPath.setText(_translate("MainWidget", "F:MyToolsPyToolsTWTools"))
        self.BlogPathSearchBtn.setText(_translate("MainWidget", "浏览"))
        self.DeployBtn.setText(_translate("MainWidget", "部署"))
        self.OpenPostPathBtn.setText(_translate("MainWidget", "打开文章目录"))
        self.OpenBlogPathBtn.setText(_translate("MainWidget", "打开博客目录"))
        self.DeployPushBtn.setText(_translate("MainWidget", "部署并推送"))
        self.DebugBtn.setText(_translate("MainWidget", "Debug调试"))
        self.CreatPostBtn.setText(_translate("MainWidget", "创建文章"))
