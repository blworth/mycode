import os.path

fileName = ""

test = (".txt", ".py", ".index", ".csv", ".xslx", ".jpg", ".xls", ".doc", ".xml", ".zip", ".rar")

while fileName != fileName.endswith(test):
    fileName = input("What would you like to name the file?")
    if fileName.endswith(test):
        break

fileContains = input("What would you like to write in the file?")


with open(fileName, "w") as newFile:
    print(fileContains, file=newFile)

if os.path.exists(fileName):
    print(f"The file: {fileName} exists!")
else:
    print(f"The file: {fileName} does not exist!")
