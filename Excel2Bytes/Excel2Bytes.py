import os

from ExcelUtil import CopyScripts, CopyBytes
from FieldGenerate import GenerateFieldBytes, GenerateLNGBytes
from LanguageUtil import InitLanguage, SaveLanguage
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
    # GenerateFieldBytes(os.path.join(TablePath, 'Text.xlsx'), "SystemArray")
    GenerateLNGBytes('Language')
    SaveLanguage()
    CopyExportFiles()
    # CreateTableManagerCs()

