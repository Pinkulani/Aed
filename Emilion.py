from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Home(object):
    def __init__(self):
        pass

    def Draw(self):
        Label = LabelFrame(FrameRight, text = "Test Frame", bg = "Orange")
        Label.place(x = 10, y = 10, width = 500, height = 500)

class Storage(object):
    def __init__(self):
        pass

    def Draw(self):
        Label = LabelFrame(FrameRight, text = "Test Frame", bg = "Yellow")
        Label.place(x = 10, y = 10, width = 500, height = 500)

class Calculator(object):
    def __init__(self):
        pass

    def Draw(self):
        Label = LabelFrame(FrameRight, text = "Test Frame", bg = "Green")
        Label.place(x = 10, y = 10, width = 500, height = 500)

class Timer(object):
    def __init__(self):
        pass

    def Draw(self):
        Label = LabelFrame(FrameRight, text = "Test Frame", bg = "Cyan")
        Label.place(x = 10, y = 10, width = 500, height = 500)

class Colorpicker(object):
    def __init__(self):
        pass

    def Draw(self):
        Label = LabelFrame(FrameRight, text = "Test Frame", bg = "Blue")
        Label.place(x = 10, y = 10, width = 500, height = 500)

class Notes(object):
    def __init__(self):
        pass

    def Draw(self):
        Label = LabelFrame(FrameRight, text = "Test Frame", bg = "Purple")
        Label.place(x = 10, y = 10, width = 500, height = 500)

class Contacts(object):
    def __init__(self):
        pass

    def Draw(self):
        Label = LabelFrame(FrameRight, text = "Test Frame", bg = "Pink")
        Label.place(x = 10, y = 10, width = 500, height = 500)

class Clock(object):
    def __init__(self):
        pass

    def Draw(self):
        Label = LabelFrame(FrameRight, text = "Test Frame", bg = "Yellow")
        Label.place(x = 10, y = 10, width = 500, height = 500)

class Destructor(object):
    def __init__(self):
        pass
    def Destroy():
        pass

# Run Number (App) that is listed in Order
class Helper(object):
    def __init__(self):
        pass
    def Run(self, Number):
        match Number: # Apps
            case 0:
                print("Home")
                Home.Draw(self)
            case 1:
                print("Storage")
                Storage.Draw(self)
            case 2:
                print("Calculator") 
                Calculator.Draw(self)
            case 3:
                print("Timer") 
                Timer.Draw(self)
            case 4:
                print("Colorpicker")
                Colorpicker.Draw(self) 
            case 5:
                print("Notes") 
                Notes.Draw(self)
            case 6:
                print("Contacts") 
                Contacts.Draw(self)
            case 7:
                print("Clock")
                Clock.Draw(self)
            case 8:
                print("Quit")
                quit()
            case _: # Error
                print("File not found")
                messagebox.showerror("Error", "App is not installed.")

# Class Setup
Helper = Helper()

# Setup
Emilion = Tk()
Emilion.title("Emilion")
Emilion.geometry("500x500")

Style = ttk.Style()
Style.theme_use("clam")

# Window
Window = ttk.PanedWindow(Emilion, orient = HORIZONTAL)
Window.place(x = 0 , y = 0, width = 3000 , height = 3000)

# Frames
FrameLeft = Frame(Window, bg = "Cyan", relief = "ridge") # Blue Window
Window.add(FrameLeft, weight = 2) # Start position of Slider

FrameRight = Frame(Window, bg = "Red", relief = "ridge") # Red Window
Window.add(FrameRight, weight = 30)

# Icons that will appear
Icons = ("Home", "Storage", "Calculator", "Timer", "Colorpicker", "Notes", "Contacts", "Clock", "Quit")

# Draw Menu
Distance = 0
ButtonIcons = []
for i in range(len(Icons)): # Go through list of Icons and place with Run command from Helper class
    ButtonIcons.append(Button(FrameLeft, text = Icons[i], relief = "ridge", font = ("", 10), command = lambda x = i:Helper.Run(x)))
    ButtonIcons[i].place(x = 0, y = Distance, width = 64, height = 32) # Place under each other
    Distance += 32

# Loop
Emilion.minsize(500, 500)
Emilion.mainloop()
