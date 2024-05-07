import os
from tkinter import *
#Consider
from tkinter import filedialog #Ask Cosme what this is for versus *
#from tkinter import font
import FileManagerOld
os.system('cls')

# x create
# a - append
# w - write will create a file

# valid_string = r"C:\Users\antho\Desktop\Coding\textEditor\textfilecosme5.txt"
# temp_file = open(valid_string, "x")
# print(temp_file.read())
#Something you can type with
#create new tab---------------------------------------------------------------------------------------------
class FileManager():
    def __init__(self, file_directory = None, name_of_file = None):
        self.file_directory = file_directory
        self.name_of_file = name_of_file

    def read_file():
        pass

test = FileManagerOld.FileManager()

