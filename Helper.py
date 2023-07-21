from tkinter import *
from tkinter import messagebox

from Home.Home import Home

class Helper(object):
    def __init__(self):
        self.Number = -1
    def Run(self, Number):
        match Number: # Apps
            case 0:
                print("Home")  
            case 1:
                print("Storage")
            case 2:
                print("Calculator") 
            case 3:
                print("Timer") 
            case 4:
                print("Colorpicker") 
            case 5:
                print("Notes") 
            case 6:
                print("Contacts") 
            case 7:
                print("Chat") 
            case 8:
                print("Clock")
            case 9:
                print("Terminal") 
            case 10:
                print("Test")
                Home.test(self)

            case _: # Error
                print("File not found")
                messagebox.showerror("Error", "File was not found.")
