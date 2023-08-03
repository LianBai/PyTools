# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TipWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_TipWidget(object):
    def setupUi(self, TipWidget):
        if not TipWidget.objectName():
            TipWidget.setObjectName(u"TipWidget")
        TipWidget.setWindowModality(Qt.WindowModal)
        TipWidget.setEnabled(False)
        TipWidget.resize(200, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TipWidget.sizePolicy().hasHeightForWidth())
        TipWidget.setSizePolicy(sizePolicy)
        TipWidget.setMinimumSize(QSize(200, 100))
        TipWidget.setMaximumSize(QSize(200, 100))
        icon = QIcon()
        icon.addFile(u"TWTools.ico", QSize(), QIcon.Normal, QIcon.Off)
        TipWidget.setWindowIcon(icon)
        TipWidget.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(TipWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(TipWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(TipWidget)

        QMetaObject.connectSlotsByName(TipWidget)
    # setupUi

    def retranslateUi(self, TipWidget):
        TipWidget.setWindowTitle(QCoreApplication.translate("TipWidget", u"\u63d0\u793a", None))
        self.label.setText(QCoreApplication.translate("TipWidget", u"TextLabel", None))
    # retranslateUi

