import os

from AppUtil import ShowTipDialog


def DeleteDir(dirPath, logWidget):
    logWidget.append(f"取消软链目录: {dirPath}")
    if os.path.exists(dirPath):
        if not os.path.islink(dirPath):
            logWidget.append(f"存在无法识别的软链目录：{dirPath}")
        os.unlink(dirPath)  # 删除符号链接文件
        if os.path.exists(dirPath):
            logWidget.append(f"删除软链目录：{dirPath}")
            os.rmdir(dirPath)


def MakeLink(source, destination, logWidget):
    DeleteDir(destination, logWidget)
    logWidget.append(f"创建软链接: {destination} -> {source}")
    if not os.path.exists(destination):
        os.symlink(source, destination, target_is_directory=True)
    else:
        logWidget.append(f"git已存在相同的svn目录：{destination} {os.path.islink(destination)}")


def OpenPath(path, widget):
    if os.path.exists(path):
        os.startfile(path)
    else:
        ShowTipDialog("错误", f"路径不存在：{path}", widget)

