# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'roommain.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.setEnabled(True)
        Form.resize(342, 420)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(342, 420))
        Form.setMaximumSize(QSize(16777215, 16777215))
        Form.setSizeIncrement(QSize(0, 0))
        Form.setBaseSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ResLink = QLabel(Form)
        self.ResLink.setObjectName(u"ResLink")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.ResLink.setFont(font)
        self.ResLink.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ResLink, 0, 0, 2, 2)

        self.UpdateBtn = QPushButton(Form)
        self.UpdateBtn.setObjectName(u"UpdateBtn")

        self.gridLayout_2.addWidget(self.UpdateBtn, 0, 2, 1, 2)

        self.ResLinkRefBtn = QPushButton(Form)
        self.ResLinkRefBtn.setObjectName(u"ResLinkRefBtn")

        self.gridLayout_2.addWidget(self.ResLinkRefBtn, 1, 2, 1, 2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.ProPath = QLabel(Form)
        self.ProPath.setObjectName(u"ProPath")
        self.ProPath.setScaledContents(True)
        self.ProPath.setAlignment(Qt.AlignCenter)
        self.ProPath.setWordWrap(False)

        self.gridLayout_2.addWidget(self.ProPath, 2, 1, 1, 2)

        self.ProPathSearchBtn = QPushButton(Form)
        self.ProPathSearchBtn.setObjectName(u"ProPathSearchBtn")

        self.gridLayout_2.addWidget(self.ProPathSearchBtn, 2, 3, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.SvnPath = QLabel(Form)
        self.SvnPath.setObjectName(u"SvnPath")
        self.SvnPath.setScaledContents(True)
        self.SvnPath.setAlignment(Qt.AlignCenter)
        self.SvnPath.setWordWrap(False)

        self.gridLayout_2.addWidget(self.SvnPath, 3, 1, 1, 2)

        self.SvnPathSearchBtn = QPushButton(Form)
        self.SvnPathSearchBtn.setObjectName(u"SvnPathSearchBtn")

        self.gridLayout_2.addWidget(self.SvnPathSearchBtn, 3, 3, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.SvnExePath = QLabel(Form)
        self.SvnExePath.setObjectName(u"SvnExePath")
        self.SvnExePath.setScaledContents(True)
        self.SvnExePath.setAlignment(Qt.AlignCenter)
        self.SvnExePath.setWordWrap(True)

        self.gridLayout_2.addWidget(self.SvnExePath, 4, 1, 1, 2)

        self.SvnExeSearchBtn = QPushButton(Form)
        self.SvnExeSearchBtn.setObjectName(u"SvnExeSearchBtn")

        self.gridLayout_2.addWidget(self.SvnExeSearchBtn, 4, 3, 1, 1)

        self.BtnsLayout = QGridLayout()
        self.BtnsLayout.setObjectName(u"BtnsLayout")
        self.ResDevBtn = QPushButton(Form)
        self.ResDevBtn.setObjectName(u"ResDevBtn")
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferDefault)
        self.ResDevBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.ResDevBtn, 5, 0, 1, 1)

        self.OpenExcelPathBtn = QPushButton(Form)
        self.OpenExcelPathBtn.setObjectName(u"OpenExcelPathBtn")
        self.OpenExcelPathBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.OpenExcelPathBtn, 0, 2, 1, 1)

        self.OpenReleasePathBtn = QPushButton(Form)
        self.OpenReleasePathBtn.setObjectName(u"OpenReleasePathBtn")
        self.OpenReleasePathBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.OpenReleasePathBtn, 4, 1, 1, 1)

        self.OpenAndroidPath = QPushButton(Form)
        self.OpenAndroidPath.setObjectName(u"OpenAndroidPath")
        self.OpenAndroidPath.setFont(font1)

        self.BtnsLayout.addWidget(self.OpenAndroidPath, 3, 1, 1, 1)

        self.OpenProPathBtn = QPushButton(Form)
        self.OpenProPathBtn.setObjectName(u"OpenProPathBtn")
        self.OpenProPathBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.OpenProPathBtn, 0, 0, 1, 1)

        self.GuideProtobufBtn = QPushButton(Form)
        self.GuideProtobufBtn.setObjectName(u"GuideProtobufBtn")
        self.GuideProtobufBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.GuideProtobufBtn, 1, 2, 1, 1)

        self.OpenSvnPathBtn = QPushButton(Form)
        self.OpenSvnPathBtn.setObjectName(u"OpenSvnPathBtn")
        self.OpenSvnPathBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.OpenSvnPathBtn, 0, 1, 1, 1)

        self.GuideTabelBtn = QPushButton(Form)
        self.GuideTabelBtn.setObjectName(u"GuideTabelBtn")
        self.GuideTabelBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.GuideTabelBtn, 1, 0, 1, 1)

        self.SvnCommitBtn = QPushButton(Form)
        self.SvnCommitBtn.setObjectName(u"SvnCommitBtn")
        self.SvnCommitBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.SvnCommitBtn, 1, 1, 1, 1)

        self.OpenTrunkPathBtn = QPushButton(Form)
        self.OpenTrunkPathBtn.setObjectName(u"OpenTrunkPathBtn")
        self.OpenTrunkPathBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.OpenTrunkPathBtn, 4, 2, 1, 1)

        self.OpenServerPathBtn = QPushButton(Form)
        self.OpenServerPathBtn.setObjectName(u"OpenServerPathBtn")
        self.OpenServerPathBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.OpenServerPathBtn, 2, 0, 1, 1)

        self.OpenProtobufPathBtn = QPushButton(Form)
        self.OpenProtobufPathBtn.setObjectName(u"OpenProtobufPathBtn")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.OpenProtobufPathBtn.setFont(font2)

        self.BtnsLayout.addWidget(self.OpenProtobufPathBtn, 3, 0, 1, 1)

        self.ResReleaseBtn = QPushButton(Form)
        self.ResReleaseBtn.setObjectName(u"ResReleaseBtn")
        self.ResReleaseBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.ResReleaseBtn, 5, 1, 1, 1)

        self.ResTrunkBtn = QPushButton(Form)
        self.ResTrunkBtn.setObjectName(u"ResTrunkBtn")
        self.ResTrunkBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.ResTrunkBtn, 5, 2, 1, 1)

        self.OpenServerBtn = QPushButton(Form)
        self.OpenServerBtn.setObjectName(u"OpenServerBtn")
        self.OpenServerBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.OpenServerBtn, 2, 1, 1, 1)

        self.OpenDevPathBtn = QPushButton(Form)
        self.OpenDevPathBtn.setObjectName(u"OpenDevPathBtn")
        self.OpenDevPathBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.OpenDevPathBtn, 4, 0, 1, 1)

        self.CloseServerBtn = QPushButton(Form)
        self.CloseServerBtn.setObjectName(u"CloseServerBtn")
        self.CloseServerBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.CloseServerBtn, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.BtnsLayout, 5, 0, 1, 4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5de5\u5177", None))
        self.ResLink.setText(QCoreApplication.translate("Form", u"DEV", None))
        self.UpdateBtn.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u66f4\u65b0", None))
        self.ResLinkRefBtn.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u8def\u5f84", None))
        self.ProPath.setText("")
        self.ProPathSearchBtn.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"SVN\u8def\u5f84", None))
        self.SvnPath.setText("")
        self.SvnPathSearchBtn.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"svn\u8f6f\u4ef6\u8def\u5f84", None))
        self.SvnExePath.setText("")
        self.SvnExeSearchBtn.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.ResDevBtn.setText(QCoreApplication.translate("Form", u"\u5207\u6362\u6210dev\u8d44\u6e90", None))
        self.OpenExcelPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u8868\u683c\u76ee\u5f55", None))
        self.OpenReleasePathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00Release\u76ee\u5f55", None))
        self.OpenAndroidPath.setText(QCoreApplication.translate("Form", u"\u6253\u5f00Android\u76ee\u5f55", None))
        self.OpenProPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u9879\u76ee\u76ee\u5f55", None))
        self.GuideProtobufBtn.setText(QCoreApplication.translate("Form", u"\u5bfc\u534f\u8bae", None))
        self.OpenSvnPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00SVN\u76ee\u5f55", None))
        self.GuideTabelBtn.setText(QCoreApplication.translate("Form", u"\u5bfc\u8868", None))
        self.SvnCommitBtn.setText(QCoreApplication.translate("Form", u"Svn\u63d0\u4ea4", None))
        self.OpenTrunkPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00trunk\u76ee\u5f55", None))
        self.OpenServerPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u670d\u52a1\u5668\u76ee\u5f55", None))
        self.OpenProtobufPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00Protobuf\u76ee\u5f55", None))
        self.ResReleaseBtn.setText(QCoreApplication.translate("Form", u"\u5207\u6362\u6210release\u8d44\u6e90", None))
        self.ResTrunkBtn.setText(QCoreApplication.translate("Form", u"\u5207\u6362\u6210trunk\u8d44\u6e90", None))
        self.OpenServerBtn.setText(QCoreApplication.translate("Form", u"\u542f\u52a8\u672c\u5730\u670d\u52a1\u5668", None))
        self.OpenDevPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00dev\u76ee\u5f55", None))
        self.CloseServerBtn.setText(QCoreApplication.translate("Form", u"\u5173\u95ed\u672c\u5730\u670d\u52a1\u5668", None))
    # retranslateUi

