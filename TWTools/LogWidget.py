# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPlainTextEdit, QSizePolicy,
    QWidget)

class Ui_LogWidget(object):
    def setupUi(self, LogWidget):
        if not LogWidget.objectName():
            LogWidget.setObjectName(u"LogWidget")
        LogWidget.setWindowModality(Qt.WindowModal)
        LogWidget.resize(700, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LogWidget.sizePolicy().hasHeightForWidth())
        LogWidget.setSizePolicy(sizePolicy)
        LogWidget.setMinimumSize(QSize(700, 300))
        icon = QIcon()
        icon.addFile(u"TWTools.ico", QSize(), QIcon.Normal, QIcon.Off)
        LogWidget.setWindowIcon(icon)
        LogWidget.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(LogWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.logText = QPlainTextEdit(LogWidget)
        self.logText.setObjectName(u"logText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logText.sizePolicy().hasHeightForWidth())
        self.logText.setSizePolicy(sizePolicy1)
        self.logText.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.logText.setReadOnly(True)
        self.logText.setCenterOnScroll(False)

        self.gridLayout.addWidget(self.logText, 0, 0, 1, 1)


        self.retranslateUi(LogWidget)

        QMetaObject.connectSlotsByName(LogWidget)
    # setupUi

    def retranslateUi(self, LogWidget):
        LogWidget.setWindowTitle(QCoreApplication.translate("LogWidget", u"\u65e5\u5fd7", None))
        self.logText.setPlainText("")
    # retranslateUi

