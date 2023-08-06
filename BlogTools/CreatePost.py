import os

from datetime import datetime
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from CreatePostWidget import Ui_CreatePostsForm
from TipUtil import ShowTipDialog
from JsonUtil import LoadConfigJsonData, SaveConfigJsonData, LoadPostConfigJsonData, SavePostConfigJsonData
from FileUtil import OpenPath


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
        config = LoadConfigJsonData()
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
            SaveConfigJsonData(config)
        self.RefreshPostView()

    def CreateBtnClicked(self):
        if self.PostsNameLineEdit.text() == "" or self.PostsNameLineEdit.text() is None:
            ShowTipDialog("请输入文章名字", "提示", self)
        else:
            self.CreatePost()
            self.close()

    def PlostTypeComboBoxChanged(self):
        config = LoadConfigJsonData()
        config["PostsTypeIndex"] = self.PlostTypeComboBox.currentIndex()
        SaveConfigJsonData(config)
        self.RefreshPostView()

    def RefreshPostView(self):
        postConfig = LoadPostConfigJsonData()
        postName = self.PlostTypeComboBox.currentText()
        if postName in postConfig and "TitlePrefix" in postConfig[postName]:
            self.PostsCategoriesLineEdit.setText(postConfig[postName]["Categories"])
            self.PostsTagLineEdit.setText(postConfig[postName]["Tags"])
        else:
            self.PostsCategoriesLineEdit.setText(postName)
            self.PostsTagLineEdit.setText(postName)
            postConfig[postName] = {"Categories": postName, "Tags": postName, "TitlePrefix": ""}
            SavePostConfigJsonData(postConfig)

    def CreatePost(self):
        config = LoadConfigJsonData()
        postConfig = LoadPostConfigJsonData()
        postTypeName = self.PlostTypeComboBox.currentText()
        postPath = os.path.join(config["BlogPath"], "source", "_posts", postTypeName)
        if not os.path.exists(postPath):
            postPath = os.path.join(config["BlogPath"], "source", "_posts")
        originalPath = os.getcwd()
        os.chdir(postPath)
        # 获取当前时间
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        if postTypeName in postConfig and "TitlePrefix" in postConfig[postTypeName]:
            titlePrefix = postConfig[postTypeName]["TitlePrefix"]
        else:
            titlePrefix = ""
        # 创建 Markdown 文件
        filename = f'{titlePrefix}{self.PostsNameLineEdit.text()}.md'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # 写入 Markdown 文件内容
                f.write('---\n')
                f.write(f'title: {titlePrefix}{self.PostsNameLineEdit.text()}\n')
                f.write(f'categories: {self.PostsCategoriesLineEdit.text()}\n')
                f.write(f'tags: {self.PostsTagLineEdit.text()}\n')
                f.write(f'date: {str(timestamp)}\n')
                f.write('---\n\n')
            ShowTipDialog("创建成功", "成功", self)
            OpenPath(postPath, self)
        except Exception as e:
            ShowTipDialog(f"创建失败:{e}", "错误", self)
        os.chdir(originalPath)
