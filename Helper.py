from tkinter import *

from Home.Home import Home

class Helper(object):
    def __init__(self):
        self.Number = -1
    
    def Run(self, Number):
        match Number:
            case 0:
                print("Home")  
            case 1:
                print("Storage")
            case _:
                print("File not found") 

h1 = Home()
