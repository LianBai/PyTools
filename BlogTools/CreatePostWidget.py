# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreatePostWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_CreatePostsForm(object):
    def setupUi(self, CreatePostsForm):
        if not CreatePostsForm.objectName():
            CreatePostsForm.setObjectName(u"CreatePostsForm")
        CreatePostsForm.resize(360, 100)
        CreatePostsForm.setMinimumSize(QSize(360, 100))
        self.PlostTypeComboBox = QComboBox(CreatePostsForm)
        self.PlostTypeComboBox.setObjectName(u"PlostTypeComboBox")
        self.PlostTypeComboBox.setGeometry(QRect(95, 20, 170, 22))
        self.PlostTypeComboBox.setStyleSheet(u"QComboBox {text-align: center;} QComboBox::item {text-align: center;}")
        self.layoutWidget = QWidget(CreatePostsForm)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 54, 341, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.PostsNameLineEdit = QLineEdit(self.layoutWidget)
        self.PostsNameLineEdit.setObjectName(u"PostsNameLineEdit")

        self.horizontalLayout.addWidget(self.PostsNameLineEdit)

        self.CreateBtn = QPushButton(self.layoutWidget)
        self.CreateBtn.setObjectName(u"CreateBtn")

        self.horizontalLayout.addWidget(self.CreateBtn)


        self.retranslateUi(CreatePostsForm)

        QMetaObject.connectSlotsByName(CreatePostsForm)
    # setupUi

    def retranslateUi(self, CreatePostsForm):
        CreatePostsForm.setWindowTitle(QCoreApplication.translate("CreatePostsForm", u"Form", None))
        self.PlostTypeComboBox.setCurrentText("")
        self.label.setText(QCoreApplication.translate("CreatePostsForm", u"\u6587\u7ae0\u540d\u5b57", None))
        self.CreateBtn.setText(QCoreApplication.translate("CreatePostsForm", u"\u521b\u5efa", None))
    # retranslateUi

