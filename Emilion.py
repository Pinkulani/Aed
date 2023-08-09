from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Home(object):
    def __init__(self):
        pass

    def Draw(self):
        Label = LabelFrame(FrameRight, text = "Test Frame")
        Label.place(x = 10, y = 10, width = 500, height = 500)

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
            case _: # Error
                # Impossible Error pretty much since I can't implement importing Classes that work with Tkinter dynamically only hardcoded.
                print("File not found")
                messagebox.showerror("Error", "App is not installed.") 

# Class Setup
Helper = Helper()

# Setup
Height = "1000"
Widht = "1000"

Emilion = Tk()
Emilion.title("Emilion")
Emilion.geometry("1000x1000")

Style = ttk.Style()
Style.theme_use("clam")

# Window
Window = ttk.PanedWindow(Emilion, orient = HORIZONTAL)
Window.place(x = 0 , y = 0, width = 1000 , height = 1000)

# Frames
FrameLeft = Frame(Window, bg = "cyan", relief = "ridge") # Blue Window
Window.add(FrameLeft, weight = 2) # Start position of Slider

FrameRight = Frame(Window, bg = "red", relief = "ridge") # Red Window
Window.add(FrameRight, weight = 30)

# Icons that will appear
Icons = ("Home", "Storage", "Calculator", "Timer", "Colorpicker", "Notes", "Contacts", "Chat", "Clock", "Terminal", "Test")

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
