from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics


def AutoLabelFontSize(label):
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
