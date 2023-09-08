import sys

from PyQt5.QtWidgets import QApplication

from MainWidget import MainWindow

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
