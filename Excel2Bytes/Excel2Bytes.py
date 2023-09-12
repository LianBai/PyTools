import os

from FieldGenerate import GenerateSingleFieldBytes
from LanguageUtil import InitLanguage, SaveLanguage
from PathUtil import InitFileDir, TablePath


def InitTable():
    InitFileDir()
    InitLanguage()


if __name__ == '__main__':
    InitTable()
    GenerateSingleFieldBytes(os.path.join(TablePath,'Text.xlsx'), "System")
    SaveLanguage()
    # CreateTableManagerCs()

