from ExcelUtil import GenerateProtobufBytes, GenerateNoneBytes

filePath = "Text.xlsx"


if __name__ == '__main__':
    GenerateNoneBytes(filePath, "System", "System_N")
    GenerateProtobufBytes(filePath, "System", "System_P")