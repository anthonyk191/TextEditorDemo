import os
from tkinter import *
#Consider
from tkinter import filedialog #Ask Cosme what this is for versus *
#from tkinter import font

os.system('cls')

# x create
# a - append
# w - write will create a file

# valid_string = r"C:\Users\antho\Desktop\Coding\textEditor\textfilecosme5.txt"
# temp_file = open(valid_string, "x")
# print(temp_file.read())
#Something you can type with
#create new tab---------------------------------------------------------------------------------------------
class NewFile():
    def __init__(self, file_location = None, name_of_file = None):
        self.file_location = file_location
        self.name_of_file = name_of_file

    def open_cosme(self, name_of_file = None):
        if self.file_location and name_of_file:
            valid_string = self.file_location + "\\" + name_of_file + ".txt"
            if os.path.exists(valid_string):
                f = open(valid_string, "r")
                print(f.read())
                f.close()
            else:
                f = open(valid_string, "x")
                f.close()
        else:
            print("please provide the name of the file")
        self.name_of_file = name_of_file

    def write_cosme(self, text = None):
        if self.name_of_file:
            valid_string = self.file_location + "\\" + self.name_of_file + ".txt"
            if os.path.exists(valid_string):
                f = open(valid_string, "w")
                f.write(text)
                f.close()
                
                f = open(valid_string, "r")
                print(f.read())
                f.close()
    def append_cosme(self, text = None):
        if self.name_of_file:
            valid_string = self.file_location + "\\" + self.name_of_file + ".txt"
            if os.path.exists(valid_string):
                f = open(valid_string, "a")
                f.write(text)
                f.close()
                
                f = open(valid_string, "r")
                print(f.read())
                f.close()

file_location_sample = r"C:\Users\antho\Desktop\Coding\textEditor"
file_name_sample = "textfilecosme2"

test = NewFile()
test.file_location = file_location_sample
test.open_cosme(file_name_sample)
# test.write_cosme("Overriding this text with this")
test.append_cosme(". More stuff to come...")