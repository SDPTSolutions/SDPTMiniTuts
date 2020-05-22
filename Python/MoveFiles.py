import os
import time

path = "YOUR PATH TO CLEAN"
movePath = "PATH WHERE TO MOVE THE FILES"

def moveFile():
    files = os.listdir(path)
    for fileName in files:
        currFile = fileName.split(".")
        if len(currFile) > 1:
            os.rename(path + fileName,movePath + fileName)
    time.sleep(1)
    moveFile()

try:
    os.mkdir(movePath)
    print("Directory Created")
except:
    print("Directory Exists")

moveFile()