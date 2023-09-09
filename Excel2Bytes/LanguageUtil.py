import os
import pandas as pd
from openpyxl import load_workbook

from LogUtil import ShowLog
from PathUtil import LanguageXlsxPath

IsUpdateLng = False
CNLanguage = 'cn'
LanguageKey = ['tw','en']
LanguageDict = {}


def InitLanguage():
    ShowLog('初始化语言表')
    if not os.path.exists(LanguageXlsxPath) or CNLanguage not in pd.read_excel(LanguageXlsxPath, sheet_name=None).keys():
        SaveLangData(CNLanguage, {'c': 'c', 'ID': 'text', 'int': 'string', '编号': '文本'})
    ReadLangData(CNLanguage)
    if IsUpdateLng:
        for key in LanguageKey:
            ReadLangData(key)


def SaveLanguage():
    ShowLog('保存语言表')
    SaveLangData(CNLanguage, LanguageDict[CNLanguage])
    if IsUpdateLng:
        languageDict = {}
        for key, value in LanguageDict[CNLanguage].items():
            languageDict[key] = value
            for keyLng in LanguageKey:
                if key in LanguageDict[keyLng].keys():
                    languageDict[keyLng][key] = LanguageDict[keyLng][key]
                else:
                    languageDict[keyLng][key] = value
        for keyLng in LanguageKey:
            SaveLangData(keyLng, languageDict[keyLng])


def ReadLangData(key):
    ShowLog(f'读取语言表数据: {key}')
    # 读取Excel文件
    df = pd.read_excel(LanguageXlsxPath, sheet_name=None)
    # 判断是否包含名为key的页签
    if key not in df.keys():
        df = pd.DataFrame(columns=['c', 'c'])
        df.loc[0] = ['ID', 'text']
        df.loc[1] = ['int', 'string']
        df.loc[2] = ['编号', '文本']
        lng = {}
        for key, value in LanguageDict[CNLanguage].items():
            df.loc[len(df)] = [key, value]
            lng[key] = value
        LanguageDict[key] = lng
        SaveLangData(key, lng)
    else:
        df = pd.read_excel(LanguageXlsxPath, sheet_name=key)
        keyLng = {}
        for index, row in df.iloc[4:].iterrows():
            keyLng[row.iloc[0]] = row.iloc[1]
        LanguageDict[key] = keyLng


def SaveLangData(key, data):
    ShowLog(f'保存语言表数据: {key}')
    workbook = load_workbook(filename=LanguageXlsxPath)
    worksheet = workbook.get_sheet_by_name(key)
    worksheet.delete_rows(4, worksheet.max_row)
    for key, value in data.items():
        worksheet.append([key, value])
    workbook.save(LanguageXlsxPath)