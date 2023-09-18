import os

from ExcelUtil import CopyScripts, CopyBytes
from FieldGenerate import GenerateFieldBytes, GenerateLNGBytes
from FindGenerate import GenerateFindBytes
from LanguageUtil import InitLanguage, SaveLanguage, TableLanguageCSName
from PathUtil import InitFileDir, TablePath


def InitTable():
    InitFileDir()
    InitLanguage()


def CopyExportFiles():
    CopyScripts()
    CopyBytes()


if __name__ == '__main__':
    InitTable()
    GenerateFieldBytes(os.path.join(TablePath, 'Text.xlsx'), "System")
    GenerateFindBytes(os.path.join(TablePath, 'Level.xlsx'), "Chase", "LevelChase2")
    # GenerateFieldBytes(os.path.join(TablePath, 'Text.xlsx'), "SystemArray")
    GenerateLNGBytes(TableLanguageCSName)
    SaveLanguage()
    CopyExportFiles()
    # CreateTableManagerCs()

