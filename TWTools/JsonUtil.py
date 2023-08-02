import json
import os
import sys

# 读取JSON文件
config_file = 'Config.json'


def exe_path():
    if hasattr(sys, 'frozen'):
        path_sys = os.path.dirname(sys.executable)
        return path_sys  # 使用pyinstaller打包后的exe目录
    path_py = os.path.dirname(__file__)
    return path_py  # 没打包前的py目录


SavePath = exe_path()


def LoadJsonData():
    # # 获取Python脚本所在的工程目录
    # pro_dir = os.path.dirname(os.path.abspath(__file__))
    # 回到工程目录
    os.chdir(SavePath)
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
    else:
        # 创建JSON文件
        config = {"ProPath": ""}
        with open(config_file, 'w') as f:
            json.dump(config, f)
    return config


def SaveJsonData(config):
    # 回到工程目录
    os.chdir(SavePath)
    with open(config_file, 'w') as f:
        json.dump(config, f)
