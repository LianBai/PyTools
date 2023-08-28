import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics, QIcon, QTextCursor
from PyQt5.QtWidgets import QDialog

from LogWidget_ui import Ui_LogWidget
from TipWidget_ui import Ui_TipWidget


def AutoMultipleLabelFontSize(label):
    # 创建一个QFont对象
    font = label.font()
    # 计算字体大小的范围
    fm = QFontMetrics(font)
    min_size = 1
    max_size = 20
    # 二分查找适应的字体大小
    low, high = min_size, max_size
    while low <= high:
        mid = (low + high) // 2
        font.setPointSize(mid)
        fm = QFontMetrics(font)
        rect = fm.boundingRect(label.rect(), Qt.TextWordWrap, label.text())
        if rect.width() <= label.width() and rect.height() <= label.height():
            low = mid + 1
        else:
            high = mid - 1

    # 设置QLabel的字体
    font.setPointSize(high)
    label.setFont(font)


def AutoSingleLabelFontSize(label):
    # 创建一个QFont对象
    font = label.font()
    # 计算字体大小的范围
    fm = QFontMetrics(font)
    min_size = 1
    max_size = 20
    # 二分查找适应的字体大小
    low, high = min_size, max_size
    while low <= high:
        mid = (low + high) // 2
        font.setPointSize(mid)
        fm = QFontMetrics(font)
        rect = fm.boundingRect(label.text())
        if rect.width() <= label.width():
            low = mid + 1
        else:
            high = mid - 1

    # 设置QLabel的字体
    font.setPointSize(high)
    label.setFont(font)


def GetLayoutHeight(layout):
    return layout.sizeHint().height()


def HideLayout(layout):
    # 获取布局中的所有组件，并隐藏它们
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.hide()

    # 禁用布局
    layout.update()


def ShowLayout(layout):
    # 获取布局中的所有组件，并隐藏它们
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.show()

    # 禁用布局
    layout.setEnabled(True)
    layout.update()
    return GetLayoutHeight(layout)


def UpdateLayoutHeight(layout, height):
    rect = layout.geometry()
    rect.setHeight(height)
    layout.setGeometry(rect)
    layout.update()


class TipWidget(QDialog, Ui_TipWidget):
    def __init__(self, parent=None):
        super(TipWidget, self).__init__(parent)
        self.setWindowIcon(QIcon("TWTools.ico"))
        self.setupUi(self)


class LogWidget(QDialog, Ui_LogWidget):
    def __init__(self, parent=None):
        super(LogWidget, self).__init__(parent)
        self.setWindowIcon(QIcon("TWTools.ico"))
        self.setupUi(self)

    def append(self, msg):
        # 向日志窗口添加消息
        self.logText.appendPlainText(msg)
        self.logText.moveCursor(QTextCursor.End)
        self.logText.moveCursor(QTextCursor.End)


def ShowTipDialog(title, content, parent=None):
    dialog = TipWidget(parent)
    dialog.show()
    dialog.label.setText(content)
    AutoMultipleLabelFontSize(dialog.label)
    dialog.setWindowTitle(title)
