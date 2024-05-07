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
class FileManager():
    def __init__(self, file_location = None, file_name = None):
        self.file_location = file_location
        self.file_name = file_name

    def open_file(self):
        if self.file_location and self.file_name:
            valid_string = self.file_location + "\\" + self.file_name + ".txt"
            if os.path.exists(valid_string):
                f = open(valid_string, "r")
                print(f.read())
                f.close()
            else:
                f = open(valid_string, "x")
                f.close()
        elif self.file_location == None and self.file_name == None:
            print("please provide a name and directory for the file")
        elif self.file_location == None:
            print("please provide a directory for the file")
        elif self.file_name == None:
            print("please provide a name for the file")


    def write_file(self, text = None):
        if self.file_location and self.file_name:
            valid_string = self.file_location + "\\" + self.file_name + ".txt"
            if os.path.exists(valid_string):
                f = open(valid_string, "w")
                f.write(text)
                f.close()
                
                f = open(valid_string, "r")
                print(f.read())
                f.close()
        elif self.file_location == None and self.file_name == None:
            print("please provide a name and directory for the file")
        elif self.file_location == None:
            print("please provide a directory for the file")
        elif self.file_name == None:
            print("please provide a name for the file")
    
    def append_file(self, text = None):
        if self.file_name:
            valid_string = self.file_location + "\\" + self.file_name + ".txt"
            if os.path.exists(valid_string):
                f = open(valid_string, "a")
                f.write(text)
                f.close()
                
                f = open(valid_string, "r")
                print(f.read())
                f.close()

    def back_space(self, remove_text_amount = 1):
        if self.file_location and self.file_name:
            valid_string = self.file_location + "\\" + self.file_name + ".txt"
            #Edge Case: Updating variable remove_text_amount
            f = open(valid_string, "r")
            length_of_text = len(f.read())
            if remove_text_amount > length_of_text:
                remove_text_amount = length_of_text
            f.close()

            #Remove unnecessary text
            f = open(valid_string, "a")
            f.truncate(remove_text_amount)
            f.close()
            
            #Read the file
            f = open(valid_string, "r")
            print(f.read())
            f.close()

#Work in progress####################################
    # def parse_file(self, beginning = 0, end = None):
    #     if self.file_location and self.file_name:
    #         valid_string = self.file_location + "\\" + self.file_name + ".txt"
    #         f = open(valid_string, "r")
    #         length_of_text = len(f.read())
    #     if end == None:
    #         end = length_of_text
    #     f.seek(beginning, end)
    #     print(f.read())
    #     f.close()


file_location_sample = r"C:\Users\antho\Desktop\Coding\textEditor"
file_name_sample = "textfilecosme2"

test = FileManager()
test.file_location = file_location_sample
test.file_name = file_name_sample
test.open_file()
test.write_file("123456789")
test.back_space(5)