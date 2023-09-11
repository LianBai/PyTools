import os

from CSScriptBuilder import CSScriptBuilder
from ExcelUtil import CreateTableManagerCs
from FieldGenerate import GenerateSingleFieldBytes
from LanguageUtil import InitLanguage, SaveLanguage
from PathUtil import InitFileDir

filePath = "Text.xlsx"


def InitTable():
    InitFileDir()
    InitLanguage()


if __name__ == '__main__':
    # InitTable()
    # GenerateSingleFieldBytes(filePath, "System")
    # SaveLanguage()
    CreateTableManagerCs()




