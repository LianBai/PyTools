# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roommain.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.setEnabled(True)
        Form.resize(385, 405)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(382, 0))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setSizeIncrement(QtCore.QSize(0, 0))
        Form.setBaseSize(QtCore.QSize(0, 0))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 29, 366, 365))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.GitLink = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GitLink.sizePolicy().hasHeightForWidth())
        self.GitLink.setSizePolicy(sizePolicy)
        self.GitLink.setMinimumSize(QtCore.QSize(180, 30))
        self.GitLink.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GitLink.setFont(font)
        self.GitLink.setScaledContents(True)
        self.GitLink.setAlignment(QtCore.Qt.AlignCenter)
        self.GitLink.setWordWrap(True)
        self.GitLink.setOpenExternalLinks(False)
        self.GitLink.setObjectName("GitLink")
        self.gridLayout.addWidget(self.GitLink, 0, 1, 1, 1)
        self.GitUpdateBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GitUpdateBtn.sizePolicy().hasHeightForWidth())
        self.GitUpdateBtn.setSizePolicy(sizePolicy)
        self.GitUpdateBtn.setMaximumSize(QtCore.QSize(57, 40))
        self.GitUpdateBtn.setObjectName("GitUpdateBtn")
        self.gridLayout.addWidget(self.GitUpdateBtn, 0, 2, 1, 1)
        self.UpdateBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UpdateBtn.sizePolicy().hasHeightForWidth())
        self.UpdateBtn.setSizePolicy(sizePolicy)
        self.UpdateBtn.setMaximumSize(QtCore.QSize(57, 40))
        self.UpdateBtn.setObjectName("UpdateBtn")
        self.gridLayout.addWidget(self.UpdateBtn, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.ResLink = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResLink.sizePolicy().hasHeightForWidth())
        self.ResLink.setSizePolicy(sizePolicy)
        self.ResLink.setMinimumSize(QtCore.QSize(180, 30))
        self.ResLink.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ResLink.setFont(font)
        self.ResLink.setScaledContents(True)
        self.ResLink.setAlignment(QtCore.Qt.AlignCenter)
        self.ResLink.setWordWrap(True)
        self.ResLink.setOpenExternalLinks(False)
        self.ResLink.setObjectName("ResLink")
        self.gridLayout.addWidget(self.ResLink, 1, 1, 1, 1)
        self.SvnUpdateBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SvnUpdateBtn.sizePolicy().hasHeightForWidth())
        self.SvnUpdateBtn.setSizePolicy(sizePolicy)
        self.SvnUpdateBtn.setMaximumSize(QtCore.QSize(57, 40))
        self.SvnUpdateBtn.setObjectName("SvnUpdateBtn")
        self.gridLayout.addWidget(self.SvnUpdateBtn, 1, 2, 1, 1)
        self.ConfigBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConfigBtn.sizePolicy().hasHeightForWidth())
        self.ConfigBtn.setSizePolicy(sizePolicy)
        self.ConfigBtn.setMaximumSize(QtCore.QSize(57, 40))
        self.ConfigBtn.setObjectName("ConfigBtn")
        self.gridLayout.addWidget(self.ConfigBtn, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OpenProPathBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenProPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenProPathBtn.setSizePolicy(sizePolicy)
        self.OpenProPathBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.OpenProPathBtn.setMaximumSize(QtCore.QSize(57, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenProPathBtn.setFont(font)
        self.OpenProPathBtn.setObjectName("OpenProPathBtn")
        self.gridLayout_2.addWidget(self.OpenProPathBtn, 0, 3, 1, 1)
        self.SvnPathSearchBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SvnPathSearchBtn.sizePolicy().hasHeightForWidth())
        self.SvnPathSearchBtn.setSizePolicy(sizePolicy)
        self.SvnPathSearchBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.SvnPathSearchBtn.setMaximumSize(QtCore.QSize(57, 40))
        self.SvnPathSearchBtn.setObjectName("SvnPathSearchBtn")
        self.gridLayout_2.addWidget(self.SvnPathSearchBtn, 1, 2, 1, 1)
        self.SvnPath = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SvnPath.sizePolicy().hasHeightForWidth())
        self.SvnPath.setSizePolicy(sizePolicy)
        self.SvnPath.setMinimumSize(QtCore.QSize(180, 30))
        self.SvnPath.setMaximumSize(QtCore.QSize(16777215, 40))
        self.SvnPath.setText("")
        self.SvnPath.setScaledContents(True)
        self.SvnPath.setAlignment(QtCore.Qt.AlignCenter)
        self.SvnPath.setWordWrap(False)
        self.SvnPath.setObjectName("SvnPath")
        self.gridLayout_2.addWidget(self.SvnPath, 1, 1, 1, 1)
        self.OpenSvnPathBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenSvnPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenSvnPathBtn.setSizePolicy(sizePolicy)
        self.OpenSvnPathBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.OpenSvnPathBtn.setMaximumSize(QtCore.QSize(57, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenSvnPathBtn.setFont(font)
        self.OpenSvnPathBtn.setObjectName("OpenSvnPathBtn")
        self.gridLayout_2.addWidget(self.OpenSvnPathBtn, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 30))
        self.label_2.setMaximumSize(QtCore.QSize(50, 40))
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 30))
        self.label.setMaximumSize(QtCore.QSize(50, 40))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.ProPath = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProPath.sizePolicy().hasHeightForWidth())
        self.ProPath.setSizePolicy(sizePolicy)
        self.ProPath.setMinimumSize(QtCore.QSize(180, 30))
        self.ProPath.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ProPath.setText("")
        self.ProPath.setScaledContents(True)
        self.ProPath.setAlignment(QtCore.Qt.AlignCenter)
        self.ProPath.setWordWrap(False)
        self.ProPath.setObjectName("ProPath")
        self.gridLayout_2.addWidget(self.ProPath, 0, 1, 1, 1)
        self.ProPathSearchBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProPathSearchBtn.sizePolicy().hasHeightForWidth())
        self.ProPathSearchBtn.setSizePolicy(sizePolicy)
        self.ProPathSearchBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.ProPathSearchBtn.setMaximumSize(QtCore.QSize(57, 40))
        self.ProPathSearchBtn.setObjectName("ProPathSearchBtn")
        self.gridLayout_2.addWidget(self.ProPathSearchBtn, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ResTrunkBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResTrunkBtn.sizePolicy().hasHeightForWidth())
        self.ResTrunkBtn.setSizePolicy(sizePolicy)
        self.ResTrunkBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.ResTrunkBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ResTrunkBtn.setFont(font)
        self.ResTrunkBtn.setObjectName("ResTrunkBtn")
        self.gridLayout_3.addWidget(self.ResTrunkBtn, 5, 2, 1, 1)
        self.ExcelOpenServerBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExcelOpenServerBtn.sizePolicy().hasHeightForWidth())
        self.ExcelOpenServerBtn.setSizePolicy(sizePolicy)
        self.ExcelOpenServerBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.ExcelOpenServerBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ExcelOpenServerBtn.setFont(font)
        self.ExcelOpenServerBtn.setObjectName("ExcelOpenServerBtn")
        self.gridLayout_3.addWidget(self.ExcelOpenServerBtn, 2, 0, 1, 1)
        self.OpenServerBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenServerBtn.sizePolicy().hasHeightForWidth())
        self.OpenServerBtn.setSizePolicy(sizePolicy)
        self.OpenServerBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.OpenServerBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenServerBtn.setFont(font)
        self.OpenServerBtn.setObjectName("OpenServerBtn")
        self.gridLayout_3.addWidget(self.OpenServerBtn, 2, 1, 1, 1)
        self.ResDevBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResDevBtn.sizePolicy().hasHeightForWidth())
        self.ResDevBtn.setSizePolicy(sizePolicy)
        self.ResDevBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.ResDevBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ResDevBtn.setFont(font)
        self.ResDevBtn.setObjectName("ResDevBtn")
        self.gridLayout_3.addWidget(self.ResDevBtn, 5, 0, 1, 1)
        self.OpenReleasePathBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenReleasePathBtn.sizePolicy().hasHeightForWidth())
        self.OpenReleasePathBtn.setSizePolicy(sizePolicy)
        self.OpenReleasePathBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.OpenReleasePathBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenReleasePathBtn.setFont(font)
        self.OpenReleasePathBtn.setObjectName("OpenReleasePathBtn")
        self.gridLayout_3.addWidget(self.OpenReleasePathBtn, 4, 1, 1, 1)
        self.CloseServerBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseServerBtn.sizePolicy().hasHeightForWidth())
        self.CloseServerBtn.setSizePolicy(sizePolicy)
        self.CloseServerBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.CloseServerBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.CloseServerBtn.setFont(font)
        self.CloseServerBtn.setObjectName("CloseServerBtn")
        self.gridLayout_3.addWidget(self.CloseServerBtn, 2, 2, 1, 1)
        self.OpenDevPathBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenDevPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenDevPathBtn.setSizePolicy(sizePolicy)
        self.OpenDevPathBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.OpenDevPathBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenDevPathBtn.setFont(font)
        self.OpenDevPathBtn.setObjectName("OpenDevPathBtn")
        self.gridLayout_3.addWidget(self.OpenDevPathBtn, 4, 0, 1, 1)
        self.OpenTrunkPathBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenTrunkPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenTrunkPathBtn.setSizePolicy(sizePolicy)
        self.OpenTrunkPathBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.OpenTrunkPathBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenTrunkPathBtn.setFont(font)
        self.OpenTrunkPathBtn.setObjectName("OpenTrunkPathBtn")
        self.gridLayout_3.addWidget(self.OpenTrunkPathBtn, 4, 2, 1, 1)
        self.ResReleaseBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResReleaseBtn.sizePolicy().hasHeightForWidth())
        self.ResReleaseBtn.setSizePolicy(sizePolicy)
        self.ResReleaseBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.ResReleaseBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ResReleaseBtn.setFont(font)
        self.ResReleaseBtn.setObjectName("ResReleaseBtn")
        self.gridLayout_3.addWidget(self.ResReleaseBtn, 5, 1, 1, 1)
        self.OpenExcelPathBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenExcelPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenExcelPathBtn.setSizePolicy(sizePolicy)
        self.OpenExcelPathBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.OpenExcelPathBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenExcelPathBtn.setFont(font)
        self.OpenExcelPathBtn.setObjectName("OpenExcelPathBtn")
        self.gridLayout_3.addWidget(self.OpenExcelPathBtn, 1, 0, 1, 1)
        self.GuideProtobufBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GuideProtobufBtn.sizePolicy().hasHeightForWidth())
        self.GuideProtobufBtn.setSizePolicy(sizePolicy)
        self.GuideProtobufBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.GuideProtobufBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.GuideProtobufBtn.setFont(font)
        self.GuideProtobufBtn.setObjectName("GuideProtobufBtn")
        self.gridLayout_3.addWidget(self.GuideProtobufBtn, 1, 2, 1, 1)
        self.HubOpenPro = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HubOpenPro.sizePolicy().hasHeightForWidth())
        self.HubOpenPro.setSizePolicy(sizePolicy)
        self.HubOpenPro.setMinimumSize(QtCore.QSize(110, 30))
        self.HubOpenPro.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.HubOpenPro.setFont(font)
        self.HubOpenPro.setObjectName("HubOpenPro")
        self.gridLayout_3.addWidget(self.HubOpenPro, 0, 0, 1, 1)
        self.SvnCommitBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SvnCommitBtn.sizePolicy().hasHeightForWidth())
        self.SvnCommitBtn.setSizePolicy(sizePolicy)
        self.SvnCommitBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.SvnCommitBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.SvnCommitBtn.setFont(font)
        self.SvnCommitBtn.setObjectName("SvnCommitBtn")
        self.gridLayout_3.addWidget(self.SvnCommitBtn, 0, 1, 1, 1)
        self.GuideTabelBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GuideTabelBtn.sizePolicy().hasHeightForWidth())
        self.GuideTabelBtn.setSizePolicy(sizePolicy)
        self.GuideTabelBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.GuideTabelBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.GuideTabelBtn.setFont(font)
        self.GuideTabelBtn.setObjectName("GuideTabelBtn")
        self.gridLayout_3.addWidget(self.GuideTabelBtn, 0, 2, 1, 1)
        self.OpenServerPathBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenServerPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenServerPathBtn.setSizePolicy(sizePolicy)
        self.OpenServerPathBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.OpenServerPathBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenServerPathBtn.setFont(font)
        self.OpenServerPathBtn.setObjectName("OpenServerPathBtn")
        self.gridLayout_3.addWidget(self.OpenServerPathBtn, 1, 1, 1, 1)
        self.OpenProtobufPathBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenProtobufPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenProtobufPathBtn.setSizePolicy(sizePolicy)
        self.OpenProtobufPathBtn.setMinimumSize(QtCore.QSize(110, 30))
        self.OpenProtobufPathBtn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenProtobufPathBtn.setFont(font)
        self.OpenProtobufPathBtn.setObjectName("OpenProtobufPathBtn")
        self.gridLayout_3.addWidget(self.OpenProtobufPathBtn, 3, 0, 1, 1)
        self.OpenAndroidPath = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenAndroidPath.sizePolicy().hasHeightForWidth())
        self.OpenAndroidPath.setSizePolicy(sizePolicy)
        self.OpenAndroidPath.setMinimumSize(QtCore.QSize(110, 30))
        self.OpenAndroidPath.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OpenAndroidPath.setFont(font)
        self.OpenAndroidPath.setObjectName("OpenAndroidPath")
        self.gridLayout_3.addWidget(self.OpenAndroidPath, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TW工具"))
        self.label_4.setText(_translate("Form", "GIT "))
        self.GitLink.setText(_translate("Form", "DEVDEVDEV"))
        self.GitUpdateBtn.setText(_translate("Form", "GIT更新"))
        self.UpdateBtn.setText(_translate("Form", "G+S更新"))
        self.label_5.setText(_translate("Form", "SVN "))
        self.ResLink.setText(_translate("Form", "DEVDEVDEV"))
        self.SvnUpdateBtn.setText(_translate("Form", "SVN更新"))
        self.ConfigBtn.setText(_translate("Form", "配置"))
        self.OpenProPathBtn.setText(_translate("Form", "打开"))
        self.SvnPathSearchBtn.setText(_translate("Form", "浏览"))
        self.OpenSvnPathBtn.setText(_translate("Form", "打开"))
        self.label_2.setText(_translate("Form", "SVN路径"))
        self.label.setText(_translate("Form", "项目路径"))
        self.ProPathSearchBtn.setText(_translate("Form", "浏览"))
        self.ResTrunkBtn.setText(_translate("Form", "切换成trunk资源"))
        self.ExcelOpenServerBtn.setText(_translate("Form", "导表启动服务器"))
        self.OpenServerBtn.setText(_translate("Form", "启动本地服务器"))
        self.ResDevBtn.setText(_translate("Form", "切换成dev资源"))
        self.OpenReleasePathBtn.setText(_translate("Form", "打开Release目录"))
        self.CloseServerBtn.setText(_translate("Form", "关闭本地服务器"))
        self.OpenDevPathBtn.setText(_translate("Form", "打开dev目录"))
        self.OpenTrunkPathBtn.setText(_translate("Form", "打开trunk目录"))
        self.ResReleaseBtn.setText(_translate("Form", "切换成release资源"))
        self.OpenExcelPathBtn.setText(_translate("Form", "打开表格目录"))
        self.GuideProtobufBtn.setText(_translate("Form", "导协议"))
        self.HubOpenPro.setText(_translate("Form", "启动项目"))
        self.SvnCommitBtn.setText(_translate("Form", "Svn提交"))
        self.GuideTabelBtn.setText(_translate("Form", "导表"))
        self.OpenServerPathBtn.setText(_translate("Form", "打开服务器目录"))
        self.OpenProtobufPathBtn.setText(_translate("Form", "打开Protobuf目录"))
        self.OpenAndroidPath.setText(_translate("Form", "打开Android目录"))
