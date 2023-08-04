import os

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from CreatePostWidget import Ui_CreatePostsForm
from TipUtil import ShowTipDialog
from JsonUtil import LoadJsonData, SaveJsonData


def ShowCreatePostsDialog(parent=None):
    dialog = CreatePostsDialog(parent)
    dialog.show()
    dialog.exec()


class CreatePostsDialog(QDialog, Ui_CreatePostsForm):
    def __init__(self, parent=None):
        super(CreatePostsDialog, self).__init__(parent)
        self.setWindowIcon(QIcon("TWTools.ico"))
        self.setupUi(self)
        self.RefreshView()
        self.PlostTypeComboBox.currentIndexChanged.connect(self.PlostTypeComboBoxChanged)

    def RefreshView(self):
        config = LoadJsonData()
        self.PostsNameLineEdit.setText("")
        self.CreateBtn.clicked.connect(self.CreateBtnClicked)
        self.PlostTypeComboBox.clear()
        path = os.path.join(config["BlogPath"], "source", "_posts")
        folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        self.PlostTypeComboBox.addItems(folders)
        if "PostsTypeIndex" in config:
            self.PlostTypeComboBox.setCurrentIndex(config["PostsTypeIndex"])
        else:
            self.PlostTypeComboBox.setCurrentIndex(0)
            config["PostsTypeIndex"] = 0
            SaveJsonData(config)

    def CreateBtnClicked(self):
        if self.PostsNameLineEdit.text() == "" or self.PostsNameLineEdit.text() is None:
            ShowTipDialog("请输入文章名字", "提示", self)
        else:
            ShowTipDialog("创建成功", "提示", self)
            self.close()

    def PlostTypeComboBoxChanged(self):
        config = LoadJsonData()
        config["PostsTypeIndex"] = self.PlostTypeComboBox.currentIndex()
        SaveJsonData(config)


