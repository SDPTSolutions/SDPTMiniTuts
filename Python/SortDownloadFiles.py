
import os
import time
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

print("======== File Sorter ========")
print("   Select a Folder to Sort   ")
print("=============================")

pathToClean = filedialog.askdirectory() + "/"

pathList = ["Image Files","Document Files","Compressed Files","Audio Files","Video Files","Program Files","Other Files","$Recyle.Bin"]

imagePath = "Image Files/"
imageExtensions = ["jpg","png","jpeg","gif","bmp","tiff","svg"]

documentPath = "Document Files/"
documentExtensions = ["pptx","ppt","ods","doc","docx","xlsx","xls","pdf","txt","html","htm"]

compressedPath = "Compressed Files/"
compressedExtensions = ["zip","rar","7z","gz","arj","deb","z"]

audioPath = "Audio Files/"
audioExtensions = ["mp3","adts","wav","wma","ogg","m4a","aiff","au","aac","3gp"]

videoPath = "Video Files/"
videoExtensions = ["webm","mpg","mp4","avi","wmv","mov"]

programPath = "Program Files/"
programExtensions = ["exe","bat","cmd","msi"]

otherPath = "Other Files/"

def initFolders():
    print("Trying To Initialize Folders...\n\n")

    try:
        print("Creating Program Files Folder...")
        os.mkdir(pathToClean+programPath)
        print("Program Files Folder Created.")
    except:
        print("Program Files Folder Already Exists.")

    print("\n\n")

    try:
        print("Creating Audio Files Folder...")
        os.mkdir(pathToClean + audioPath)
        print("Creating Audio Files Created.")
    except:
        print("Audio Files Folder Already Exists.")

    print("\n\n")

    try:
        print("Creating Video Files Folder...")
        os.mkdir(pathToClean + videoPath)
        print("Creating Video Files Created.")
    except:
        print("Video Files Folder Already Exists.")

    print("\n\n")

    try:
        print("Creating Image Files Folder...")
        os.mkdir(pathToClean + imagePath)
        print("Creating Image Files Created.")
    except:
        print("Image Files Folder Already Exists.")

    print("\n\n")

    try:
        print("Creating Document Files Folder...")
        os.mkdir(pathToClean + documentPath)
        print("Creating Document Files Created.")
    except:
        print("Image Files Folder Already Exists.")

    print("\n\n")

    try:
        print("Creating Compressed Files Folder...")
        os.mkdir(pathToClean + compressedPath)
        print("Creating Compressed Files Created.")
    except:
        print("Compressed Files Folder Already Exists.")

    print("\n\n")

    try:
        print("Creating Other Files Folder...")
        os.mkdir(pathToClean + otherPath)
        print("Creating Other Files Created.")
    except:
        print("Other Files Folder Already Exists.")

def sortFiles():

    print("\n\nReading Files.. in " + pathToClean + "\n\n")

    files = os.listdir(pathToClean)

    for file in files:
        fileDivision = file.split(".")
        fileDivisionLength = len(fileDivision)
        fileExtension = fileDivision[fileDivisionLength-1].lower()
        if fileDivisionLength != 1:
            if fileExtension in imageExtensions:
                os.rename(pathToClean+file,pathToClean+imagePath+file)
                print("Moved " + file + " To Image Files Folder")
            elif fileExtension in documentExtensions:
                os.rename(pathToClean+file,pathToClean+documentPath+file)
                print("Moved " + file + " To Document Files Folder")
            elif fileExtension in compressedExtensions:
                os.rename(pathToClean + file, pathToClean + compressedPath + file)
                print("Moved " + file + " To Compressed Files Folder")
            elif fileExtension in imageExtensions:
                os.rename(pathToClean + file, pathToClean + imagePath + file)
                print("Moved " + file + " To Image Files Folder")
            elif fileExtension in videoExtensions:
                os.rename(pathToClean + file, pathToClean + videoPath + file)
                print("Moved " + file + " To Video Files Folder")
            elif fileExtension in audioExtensions:
                os.rename(pathToClean + file, pathToClean + audioPath + file)
                print("Moved " + file + " To Audio Files Folder")
            elif fileExtension in programExtensions:
                os.rename(pathToClean + file, pathToClean + programPath + file)
                print("Moved " + file + " To Program Files Folder")
            else:
                os.rename(pathToClean + file, pathToClean + otherPath + file)
                print("Moved " + file + " To Other Files Folder")
        elif file not in pathList:
            os.rename(pathToClean + file, pathToClean + otherPath + file)

if pathToClean != "/":
    initFolders()
    sortFiles()