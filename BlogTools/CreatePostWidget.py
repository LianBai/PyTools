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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_CreatePostsForm(object):
    def setupUi(self, CreatePostsForm):
        if not CreatePostsForm.objectName():
            CreatePostsForm.setObjectName(u"CreatePostsForm")
        CreatePostsForm.resize(360, 170)
        CreatePostsForm.setMinimumSize(QSize(360, 100))
        self.PlostTypeComboBox = QComboBox(CreatePostsForm)
        self.PlostTypeComboBox.setObjectName(u"PlostTypeComboBox")
        self.PlostTypeComboBox.setGeometry(QRect(95, 20, 170, 22))
        self.PlostTypeComboBox.setStyleSheet(u"QComboBox {\n"
"    text-align: center;\n"
"}")
        self.CreateBtn = QPushButton(CreatePostsForm)
        self.CreateBtn.setObjectName(u"CreateBtn")
        self.CreateBtn.setGeometry(QRect(95, 140, 170, 22))
        self.layoutWidget = QWidget(CreatePostsForm)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(13, 57, 331, 74))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.PostsNameLineEdit = QLineEdit(self.layoutWidget)
        self.PostsNameLineEdit.setObjectName(u"PostsNameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.PostsNameLineEdit)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.PostsCategoriesLineEdit = QLineEdit(self.layoutWidget)
        self.PostsCategoriesLineEdit.setObjectName(u"PostsCategoriesLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.PostsCategoriesLineEdit)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.PostsTagLineEdit = QLineEdit(self.layoutWidget)
        self.PostsTagLineEdit.setObjectName(u"PostsTagLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.PostsTagLineEdit)


        self.retranslateUi(CreatePostsForm)

        QMetaObject.connectSlotsByName(CreatePostsForm)
    # setupUi

    def retranslateUi(self, CreatePostsForm):
        CreatePostsForm.setWindowTitle(QCoreApplication.translate("CreatePostsForm", u"Form", None))
        self.PlostTypeComboBox.setCurrentText("")
        self.CreateBtn.setText(QCoreApplication.translate("CreatePostsForm", u"\u521b\u5efa", None))
        self.label.setText(QCoreApplication.translate("CreatePostsForm", u"\u6587\u7ae0\u540d\u5b57", None))
        self.label_2.setText(QCoreApplication.translate("CreatePostsForm", u"\u6587\u7ae0\u79cd\u7c7b(categories)", None))
        self.label_3.setText(QCoreApplication.translate("CreatePostsForm", u"\u6587\u7ae0\u6807\u7b7e(Tag)", None))
    # retranslateUi

