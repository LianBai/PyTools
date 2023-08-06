import json
import os
import sys

from TipUtil import ShowTipDialog

# 读取JSON文件
config_file = 'Config.json'
PostConfig_file = 'PostConfig.json'


def exe_path():
    if hasattr(sys, 'frozen'):
        path_sys = os.path.dirname(sys.executable)
        return path_sys  # 使用pyinstaller打包后的exe目录
    path_py = os.path.dirname(__file__)
    return path_py  # 没打包前的py目录


SavePath = os.path.join(exe_path(), "save")


def LoadConfigJsonData():
    return LoadJsonData(config_file)


def SaveConfigJsonData(config):
    SaveJsonData(config_file, config)


def LoadPostConfigJsonData():
    return LoadJsonData(PostConfig_file)


def SavePostConfigJsonData(config):
    SaveJsonData(PostConfig_file, config)


def LoadJsonData(jsonName):
    if not os.path.exists(SavePath):
        os.makedirs(SavePath)
    os.chdir(SavePath)
    try:
        if os.path.exists(jsonName):
            with open(jsonName, 'r', encoding="utf-8") as f:
                config = json.load(f)
        else:
            # 创建JSON文件
            config = {}
            with open(jsonName, 'w', encoding="utf-8") as f:
                json.dump(config, f)
    except Exception as e:
        ShowTipDialog(f"读取配置文件错误:{e}")
        config = {}
    return config


def SaveJsonData(jsonName, config):
    # 回到工程目录
    if not os.path.exists(SavePath):
        os.makedirs(SavePath)
    os.chdir(SavePath)
    with open(jsonName, 'w') as f:
        json.dump(config, f)
