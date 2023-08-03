import io
import os.path
import sys

from PySide6.QtWidgets import QApplication

from MainWidget import MainWindow
from JsonUtil import LoadJsonData

sys.stdout = io.TextIOWrapper(io.BytesIO(), 'utf-8', errors='ignore')
sys.stderr = io.TextIOWrapper(io.BytesIO(), 'utf-8', errors='ignore')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    config = LoadJsonData()
    if "BlogPath" in config and os.path.exists(config["BlogPath"]):
        main.BlogPath.setText(config["BlogPath"])
        main.BlogPath.setText(config["BlogPath"])
    else:
        main.BlogPathSearchBtnClicked()
    sys.exit(app.exec())
