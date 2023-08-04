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
        Form.resize(362, 418)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(362, 418))
        Form.setMaximumSize(QSize(16777215, 16777215))
        Form.setSizeIncrement(QSize(0, 0))
        Form.setBaseSize(QSize(0, 0))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 11, 344, 395))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.GitLink = QLabel(self.layoutWidget)
        self.GitLink.setObjectName(u"GitLink")
        sizePolicy1.setHeightForWidth(self.GitLink.sizePolicy().hasHeightForWidth())
        self.GitLink.setSizePolicy(sizePolicy1)
        self.GitLink.setMinimumSize(QSize(160, 30))
        self.GitLink.setMaximumSize(QSize(160, 16777215))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.GitLink.setFont(font1)
        self.GitLink.setScaledContents(True)
        self.GitLink.setAlignment(Qt.AlignCenter)
        self.GitLink.setWordWrap(False)
        self.GitLink.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.GitLink, 0, 1, 1, 3)

        self.UpdateBtn = QPushButton(self.layoutWidget)
        self.UpdateBtn.setObjectName(u"UpdateBtn")
        sizePolicy1.setHeightForWidth(self.UpdateBtn.sizePolicy().hasHeightForWidth())
        self.UpdateBtn.setSizePolicy(sizePolicy1)
        self.UpdateBtn.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.UpdateBtn, 0, 4, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.ResLink = QLabel(self.layoutWidget)
        self.ResLink.setObjectName(u"ResLink")
        sizePolicy1.setHeightForWidth(self.ResLink.sizePolicy().hasHeightForWidth())
        self.ResLink.setSizePolicy(sizePolicy1)
        self.ResLink.setMinimumSize(QSize(160, 30))
        self.ResLink.setMaximumSize(QSize(160, 16777215))
        self.ResLink.setFont(font1)
        self.ResLink.setScaledContents(True)
        self.ResLink.setAlignment(Qt.AlignCenter)
        self.ResLink.setWordWrap(False)
        self.ResLink.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.ResLink, 1, 1, 1, 3)

        self.ResLinkRefBtn = QPushButton(self.layoutWidget)
        self.ResLinkRefBtn.setObjectName(u"ResLinkRefBtn")
        sizePolicy1.setHeightForWidth(self.ResLinkRefBtn.sizePolicy().hasHeightForWidth())
        self.ResLinkRefBtn.setSizePolicy(sizePolicy1)
        self.ResLinkRefBtn.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.ResLinkRefBtn, 1, 4, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(70, 30))
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.ProPath = QLabel(self.layoutWidget)
        self.ProPath.setObjectName(u"ProPath")
        sizePolicy1.setHeightForWidth(self.ProPath.sizePolicy().hasHeightForWidth())
        self.ProPath.setSizePolicy(sizePolicy1)
        self.ProPath.setMinimumSize(QSize(160, 30))
        self.ProPath.setMaximumSize(QSize(16777215, 16777215))
        self.ProPath.setScaledContents(True)
        self.ProPath.setAlignment(Qt.AlignCenter)
        self.ProPath.setWordWrap(False)

        self.gridLayout.addWidget(self.ProPath, 2, 1, 1, 3)

        self.ProPathSearchBtn = QPushButton(self.layoutWidget)
        self.ProPathSearchBtn.setObjectName(u"ProPathSearchBtn")
        sizePolicy1.setHeightForWidth(self.ProPathSearchBtn.sizePolicy().hasHeightForWidth())
        self.ProPathSearchBtn.setSizePolicy(sizePolicy1)
        self.ProPathSearchBtn.setMinimumSize(QSize(0, 30))
        self.ProPathSearchBtn.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.ProPathSearchBtn, 2, 4, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(70, 30))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.SvnPath = QLabel(self.layoutWidget)
        self.SvnPath.setObjectName(u"SvnPath")
        sizePolicy1.setHeightForWidth(self.SvnPath.sizePolicy().hasHeightForWidth())
        self.SvnPath.setSizePolicy(sizePolicy1)
        self.SvnPath.setMinimumSize(QSize(160, 30))
        self.SvnPath.setMaximumSize(QSize(16777215, 16777215))
        self.SvnPath.setScaledContents(True)
        self.SvnPath.setAlignment(Qt.AlignCenter)
        self.SvnPath.setWordWrap(False)

        self.gridLayout.addWidget(self.SvnPath, 3, 1, 1, 3)

        self.SvnPathSearchBtn = QPushButton(self.layoutWidget)
        self.SvnPathSearchBtn.setObjectName(u"SvnPathSearchBtn")
        sizePolicy1.setHeightForWidth(self.SvnPathSearchBtn.sizePolicy().hasHeightForWidth())
        self.SvnPathSearchBtn.setSizePolicy(sizePolicy1)
        self.SvnPathSearchBtn.setMinimumSize(QSize(0, 30))
        self.SvnPathSearchBtn.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.SvnPathSearchBtn, 3, 4, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.SvnExePath = QLabel(self.layoutWidget)
        self.SvnExePath.setObjectName(u"SvnExePath")
        sizePolicy1.setHeightForWidth(self.SvnExePath.sizePolicy().hasHeightForWidth())
        self.SvnExePath.setSizePolicy(sizePolicy1)
        self.SvnExePath.setMinimumSize(QSize(160, 30))
        self.SvnExePath.setMaximumSize(QSize(16777215, 16777215))
        self.SvnExePath.setScaledContents(True)
        self.SvnExePath.setAlignment(Qt.AlignCenter)
        self.SvnExePath.setWordWrap(True)

        self.gridLayout.addWidget(self.SvnExePath, 4, 1, 1, 3)

        self.SvnExeSearchBtn = QPushButton(self.layoutWidget)
        self.SvnExeSearchBtn.setObjectName(u"SvnExeSearchBtn")
        sizePolicy1.setHeightForWidth(self.SvnExeSearchBtn.sizePolicy().hasHeightForWidth())
        self.SvnExeSearchBtn.setSizePolicy(sizePolicy1)
        self.SvnExeSearchBtn.setMinimumSize(QSize(0, 30))
        self.SvnExeSearchBtn.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.SvnExeSearchBtn, 4, 4, 1, 1)

        self.OpenProPathBtn = QPushButton(self.layoutWidget)
        self.OpenProPathBtn.setObjectName(u"OpenProPathBtn")
        sizePolicy1.setHeightForWidth(self.OpenProPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenProPathBtn.setSizePolicy(sizePolicy1)
        self.OpenProPathBtn.setMinimumSize(QSize(110, 30))
        self.OpenProPathBtn.setMaximumSize(QSize(110, 30))
        font3 = QFont()
        font3.setStyleStrategy(QFont.PreferDefault)
        self.OpenProPathBtn.setFont(font3)

        self.gridLayout.addWidget(self.OpenProPathBtn, 5, 0, 1, 2)

        self.OpenSvnPathBtn = QPushButton(self.layoutWidget)
        self.OpenSvnPathBtn.setObjectName(u"OpenSvnPathBtn")
        sizePolicy1.setHeightForWidth(self.OpenSvnPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenSvnPathBtn.setSizePolicy(sizePolicy1)
        self.OpenSvnPathBtn.setMinimumSize(QSize(110, 30))
        self.OpenSvnPathBtn.setMaximumSize(QSize(110, 30))
        self.OpenSvnPathBtn.setFont(font3)

        self.gridLayout.addWidget(self.OpenSvnPathBtn, 5, 2, 1, 1)

        self.OpenExcelPathBtn = QPushButton(self.layoutWidget)
        self.OpenExcelPathBtn.setObjectName(u"OpenExcelPathBtn")
        sizePolicy1.setHeightForWidth(self.OpenExcelPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenExcelPathBtn.setSizePolicy(sizePolicy1)
        self.OpenExcelPathBtn.setMinimumSize(QSize(110, 30))
        self.OpenExcelPathBtn.setMaximumSize(QSize(110, 30))
        self.OpenExcelPathBtn.setFont(font3)

        self.gridLayout.addWidget(self.OpenExcelPathBtn, 5, 3, 1, 2)

        self.GuideTabelBtn = QPushButton(self.layoutWidget)
        self.GuideTabelBtn.setObjectName(u"GuideTabelBtn")
        sizePolicy1.setHeightForWidth(self.GuideTabelBtn.sizePolicy().hasHeightForWidth())
        self.GuideTabelBtn.setSizePolicy(sizePolicy1)
        self.GuideTabelBtn.setMinimumSize(QSize(110, 30))
        self.GuideTabelBtn.setMaximumSize(QSize(110, 30))
        self.GuideTabelBtn.setFont(font3)

        self.gridLayout.addWidget(self.GuideTabelBtn, 6, 0, 1, 2)

        self.SvnCommitBtn = QPushButton(self.layoutWidget)
        self.SvnCommitBtn.setObjectName(u"SvnCommitBtn")
        sizePolicy1.setHeightForWidth(self.SvnCommitBtn.sizePolicy().hasHeightForWidth())
        self.SvnCommitBtn.setSizePolicy(sizePolicy1)
        self.SvnCommitBtn.setMinimumSize(QSize(110, 30))
        self.SvnCommitBtn.setMaximumSize(QSize(110, 30))
        self.SvnCommitBtn.setFont(font3)

        self.gridLayout.addWidget(self.SvnCommitBtn, 6, 2, 1, 1)

        self.GuideProtobufBtn = QPushButton(self.layoutWidget)
        self.GuideProtobufBtn.setObjectName(u"GuideProtobufBtn")
        sizePolicy1.setHeightForWidth(self.GuideProtobufBtn.sizePolicy().hasHeightForWidth())
        self.GuideProtobufBtn.setSizePolicy(sizePolicy1)
        self.GuideProtobufBtn.setMinimumSize(QSize(110, 30))
        self.GuideProtobufBtn.setMaximumSize(QSize(110, 30))
        self.GuideProtobufBtn.setFont(font3)

        self.gridLayout.addWidget(self.GuideProtobufBtn, 6, 3, 1, 2)

        self.ExcelOpenServerBtn = QPushButton(self.layoutWidget)
        self.ExcelOpenServerBtn.setObjectName(u"ExcelOpenServerBtn")
        sizePolicy1.setHeightForWidth(self.ExcelOpenServerBtn.sizePolicy().hasHeightForWidth())
        self.ExcelOpenServerBtn.setSizePolicy(sizePolicy1)
        self.ExcelOpenServerBtn.setMinimumSize(QSize(110, 30))
        self.ExcelOpenServerBtn.setMaximumSize(QSize(110, 30))
        self.ExcelOpenServerBtn.setFont(font3)

        self.gridLayout.addWidget(self.ExcelOpenServerBtn, 7, 0, 1, 2)

        self.OpenServerBtn = QPushButton(self.layoutWidget)
        self.OpenServerBtn.setObjectName(u"OpenServerBtn")
        sizePolicy1.setHeightForWidth(self.OpenServerBtn.sizePolicy().hasHeightForWidth())
        self.OpenServerBtn.setSizePolicy(sizePolicy1)
        self.OpenServerBtn.setMinimumSize(QSize(110, 30))
        self.OpenServerBtn.setMaximumSize(QSize(110, 30))
        self.OpenServerBtn.setFont(font3)

        self.gridLayout.addWidget(self.OpenServerBtn, 7, 2, 1, 1)

        self.CloseServerBtn = QPushButton(self.layoutWidget)
        self.CloseServerBtn.setObjectName(u"CloseServerBtn")
        sizePolicy1.setHeightForWidth(self.CloseServerBtn.sizePolicy().hasHeightForWidth())
        self.CloseServerBtn.setSizePolicy(sizePolicy1)
        self.CloseServerBtn.setMinimumSize(QSize(110, 30))
        self.CloseServerBtn.setMaximumSize(QSize(110, 30))
        self.CloseServerBtn.setFont(font3)

        self.gridLayout.addWidget(self.CloseServerBtn, 7, 3, 1, 2)

        self.OpenServerPathBtn = QPushButton(self.layoutWidget)
        self.OpenServerPathBtn.setObjectName(u"OpenServerPathBtn")
        sizePolicy1.setHeightForWidth(self.OpenServerPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenServerPathBtn.setSizePolicy(sizePolicy1)
        self.OpenServerPathBtn.setMinimumSize(QSize(110, 30))
        self.OpenServerPathBtn.setMaximumSize(QSize(110, 30))
        self.OpenServerPathBtn.setFont(font3)

        self.gridLayout.addWidget(self.OpenServerPathBtn, 8, 0, 1, 2)

        self.OpenProtobufPathBtn = QPushButton(self.layoutWidget)
        self.OpenProtobufPathBtn.setObjectName(u"OpenProtobufPathBtn")
        sizePolicy1.setHeightForWidth(self.OpenProtobufPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenProtobufPathBtn.setSizePolicy(sizePolicy1)
        self.OpenProtobufPathBtn.setMinimumSize(QSize(110, 30))
        self.OpenProtobufPathBtn.setMaximumSize(QSize(110, 30))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.OpenProtobufPathBtn.setFont(font4)

        self.gridLayout.addWidget(self.OpenProtobufPathBtn, 8, 2, 1, 1)

        self.OpenAndroidPath = QPushButton(self.layoutWidget)
        self.OpenAndroidPath.setObjectName(u"OpenAndroidPath")
        sizePolicy1.setHeightForWidth(self.OpenAndroidPath.sizePolicy().hasHeightForWidth())
        self.OpenAndroidPath.setSizePolicy(sizePolicy1)
        self.OpenAndroidPath.setMinimumSize(QSize(110, 30))
        self.OpenAndroidPath.setMaximumSize(QSize(110, 30))
        self.OpenAndroidPath.setFont(font3)

        self.gridLayout.addWidget(self.OpenAndroidPath, 8, 3, 1, 2)

        self.OpenDevPathBtn = QPushButton(self.layoutWidget)
        self.OpenDevPathBtn.setObjectName(u"OpenDevPathBtn")
        sizePolicy1.setHeightForWidth(self.OpenDevPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenDevPathBtn.setSizePolicy(sizePolicy1)
        self.OpenDevPathBtn.setMinimumSize(QSize(110, 30))
        self.OpenDevPathBtn.setMaximumSize(QSize(110, 30))
        self.OpenDevPathBtn.setFont(font3)

        self.gridLayout.addWidget(self.OpenDevPathBtn, 9, 0, 1, 2)

        self.OpenReleasePathBtn = QPushButton(self.layoutWidget)
        self.OpenReleasePathBtn.setObjectName(u"OpenReleasePathBtn")
        sizePolicy1.setHeightForWidth(self.OpenReleasePathBtn.sizePolicy().hasHeightForWidth())
        self.OpenReleasePathBtn.setSizePolicy(sizePolicy1)
        self.OpenReleasePathBtn.setMinimumSize(QSize(110, 30))
        self.OpenReleasePathBtn.setMaximumSize(QSize(110, 30))
        self.OpenReleasePathBtn.setFont(font3)

        self.gridLayout.addWidget(self.OpenReleasePathBtn, 9, 2, 1, 1)

        self.OpenTrunkPathBtn = QPushButton(self.layoutWidget)
        self.OpenTrunkPathBtn.setObjectName(u"OpenTrunkPathBtn")
        sizePolicy1.setHeightForWidth(self.OpenTrunkPathBtn.sizePolicy().hasHeightForWidth())
        self.OpenTrunkPathBtn.setSizePolicy(sizePolicy1)
        self.OpenTrunkPathBtn.setMinimumSize(QSize(110, 30))
        self.OpenTrunkPathBtn.setMaximumSize(QSize(110, 30))
        self.OpenTrunkPathBtn.setFont(font3)

        self.gridLayout.addWidget(self.OpenTrunkPathBtn, 9, 3, 1, 2)

        self.ResDevBtn = QPushButton(self.layoutWidget)
        self.ResDevBtn.setObjectName(u"ResDevBtn")
        sizePolicy1.setHeightForWidth(self.ResDevBtn.sizePolicy().hasHeightForWidth())
        self.ResDevBtn.setSizePolicy(sizePolicy1)
        self.ResDevBtn.setMinimumSize(QSize(110, 30))
        self.ResDevBtn.setMaximumSize(QSize(110, 30))
        self.ResDevBtn.setFont(font3)

        self.gridLayout.addWidget(self.ResDevBtn, 10, 0, 1, 2)

        self.ResReleaseBtn = QPushButton(self.layoutWidget)
        self.ResReleaseBtn.setObjectName(u"ResReleaseBtn")
        sizePolicy1.setHeightForWidth(self.ResReleaseBtn.sizePolicy().hasHeightForWidth())
        self.ResReleaseBtn.setSizePolicy(sizePolicy1)
        self.ResReleaseBtn.setMinimumSize(QSize(110, 30))
        self.ResReleaseBtn.setMaximumSize(QSize(110, 30))
        self.ResReleaseBtn.setFont(font3)

        self.gridLayout.addWidget(self.ResReleaseBtn, 10, 2, 1, 1)

        self.ResTrunkBtn = QPushButton(self.layoutWidget)
        self.ResTrunkBtn.setObjectName(u"ResTrunkBtn")
        sizePolicy1.setHeightForWidth(self.ResTrunkBtn.sizePolicy().hasHeightForWidth())
        self.ResTrunkBtn.setSizePolicy(sizePolicy1)
        self.ResTrunkBtn.setMinimumSize(QSize(110, 30))
        self.ResTrunkBtn.setMaximumSize(QSize(110, 30))
        self.ResTrunkBtn.setFont(font3)

        self.gridLayout.addWidget(self.ResTrunkBtn, 10, 3, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5de5\u5177", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"GIT ", None))
        self.GitLink.setText(QCoreApplication.translate("Form", u"DEVDEVDEV", None))
        self.UpdateBtn.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u66f4\u65b0", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"SVN ", None))
        self.ResLink.setText(QCoreApplication.translate("Form", u"DEVDEVDEV", None))
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
        self.OpenProPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u9879\u76ee\u76ee\u5f55", None))
        self.OpenSvnPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00SVN\u76ee\u5f55", None))
        self.OpenExcelPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u8868\u683c\u76ee\u5f55", None))
        self.GuideTabelBtn.setText(QCoreApplication.translate("Form", u"\u5bfc\u8868", None))
        self.SvnCommitBtn.setText(QCoreApplication.translate("Form", u"Svn\u63d0\u4ea4", None))
        self.GuideProtobufBtn.setText(QCoreApplication.translate("Form", u"\u5bfc\u534f\u8bae", None))
        self.ExcelOpenServerBtn.setText(QCoreApplication.translate("Form", u"\u5bfc\u8868\u542f\u52a8\u670d\u52a1\u5668", None))
        self.OpenServerBtn.setText(QCoreApplication.translate("Form", u"\u542f\u52a8\u672c\u5730\u670d\u52a1\u5668", None))
        self.CloseServerBtn.setText(QCoreApplication.translate("Form", u"\u5173\u95ed\u672c\u5730\u670d\u52a1\u5668", None))
        self.OpenServerPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u670d\u52a1\u5668\u76ee\u5f55", None))
        self.OpenProtobufPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00Protobuf\u76ee\u5f55", None))
        self.OpenAndroidPath.setText(QCoreApplication.translate("Form", u"\u6253\u5f00Android\u76ee\u5f55", None))
        self.OpenDevPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00dev\u76ee\u5f55", None))
        self.OpenReleasePathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00Release\u76ee\u5f55", None))
        self.OpenTrunkPathBtn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00trunk\u76ee\u5f55", None))
        self.ResDevBtn.setText(QCoreApplication.translate("Form", u"\u5207\u6362\u6210dev\u8d44\u6e90", None))
        self.ResReleaseBtn.setText(QCoreApplication.translate("Form", u"\u5207\u6362\u6210release\u8d44\u6e90", None))
        self.ResTrunkBtn.setText(QCoreApplication.translate("Form", u"\u5207\u6362\u6210trunk\u8d44\u6e90", None))
    # retranslateUi

