# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetMain.ui'
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

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.setWindowModality(Qt.WindowModal)
        MainWidget.setEnabled(True)
        MainWidget.resize(293, 118)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        MainWidget.setMinimumSize(QSize(0, 0))
        MainWidget.setMaximumSize(QSize(16777215, 16777215))
        MainWidget.setSizeIncrement(QSize(0, 0))
        MainWidget.setBaseSize(QSize(0, 0))
        self.gridLayout = QGridLayout(MainWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.BlogLabel = QLabel(MainWidget)
        self.BlogLabel.setObjectName(u"BlogLabel")

        self.gridLayout.addWidget(self.BlogLabel, 0, 0, 1, 1)

        self.BlogPath = QLabel(MainWidget)
        self.BlogPath.setObjectName(u"BlogPath")
        self.BlogPath.setMinimumSize(QSize(140, 40))
        self.BlogPath.setMaximumSize(QSize(140, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.BlogPath.setFont(font)
        self.BlogPath.setAutoFillBackground(False)
        self.BlogPath.setScaledContents(True)
        self.BlogPath.setAlignment(Qt.AlignCenter)
        self.BlogPath.setWordWrap(True)

        self.gridLayout.addWidget(self.BlogPath, 0, 1, 1, 1)

        self.BlogPathSearchBtn = QPushButton(MainWidget)
        self.BlogPathSearchBtn.setObjectName(u"BlogPathSearchBtn")

        self.gridLayout.addWidget(self.BlogPathSearchBtn, 0, 2, 1, 1)

        self.BtnsLayout = QGridLayout()
        self.BtnsLayout.setObjectName(u"BtnsLayout")
        self.DeployBtn = QPushButton(MainWidget)
        self.DeployBtn.setObjectName(u"DeployBtn")
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferDefault)
        self.DeployBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.DeployBtn, 0, 1, 1, 1)

        self.OpenPostPathBtn = QPushButton(MainWidget)
        self.OpenPostPathBtn.setObjectName(u"OpenPostPathBtn")
        self.OpenPostPathBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.OpenPostPathBtn, 1, 1, 1, 1)

        self.OpenBlogPathBtn = QPushButton(MainWidget)
        self.OpenBlogPathBtn.setObjectName(u"OpenBlogPathBtn")
        self.OpenBlogPathBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.OpenBlogPathBtn, 1, 0, 1, 1)

        self.DeployPushBtn = QPushButton(MainWidget)
        self.DeployPushBtn.setObjectName(u"DeployPushBtn")
        self.DeployPushBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.DeployPushBtn, 0, 2, 1, 1)

        self.DebugBtn = QPushButton(MainWidget)
        self.DebugBtn.setObjectName(u"DebugBtn")
        self.DebugBtn.setEnabled(True)
        self.DebugBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.DebugBtn, 0, 0, 1, 1)

        self.CreatPostBtn = QPushButton(MainWidget)
        self.CreatPostBtn.setObjectName(u"CreatPostBtn")
        self.CreatPostBtn.setFont(font1)

        self.BtnsLayout.addWidget(self.CreatPostBtn, 1, 2, 1, 1)


        self.gridLayout.addLayout(self.BtnsLayout, 1, 0, 1, 3)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"\u5de5\u5177", None))
        self.BlogLabel.setText(QCoreApplication.translate("MainWidget", u"\u9879\u76ee\u8def\u5f84", None))
        self.BlogPath.setText(QCoreApplication.translate("MainWidget", u"F:MyToolsPyToolsTWTools", None))
        self.BlogPathSearchBtn.setText(QCoreApplication.translate("MainWidget", u"\u6d4f\u89c8", None))
        self.DeployBtn.setText(QCoreApplication.translate("MainWidget", u"\u90e8\u7f72", None))
        self.OpenPostPathBtn.setText(QCoreApplication.translate("MainWidget", u"\u6253\u5f00\u6587\u7ae0\u76ee\u5f55", None))
        self.OpenBlogPathBtn.setText(QCoreApplication.translate("MainWidget", u"\u6253\u5f00\u535a\u5ba2\u76ee\u5f55", None))
        self.DeployPushBtn.setText(QCoreApplication.translate("MainWidget", u"\u90e8\u7f72\u5e76\u63a8\u9001", None))
        self.DebugBtn.setText(QCoreApplication.translate("MainWidget", u"Debug\u8c03\u8bd5", None))
        self.CreatPostBtn.setText(QCoreApplication.translate("MainWidget", u"\u521b\u5efa\u6587\u7ae0", None))
    # retranslateUi

