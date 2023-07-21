from tkinter import *
from tkinter import ttk
from Helper import Helper

# Setup
Height = "1000"
Widht = "1000"

Emilion = Tk()
Emilion.title("Emilion 🥕")
Emilion.geometry("1000x1000")

Style = ttk.Style()
Style.theme_use("clam")

Helper = Helper()

# Icons
Icons = ("Home", "Storage", "Calculator", "Timer", "Colorpicker", "Notes", "Contacts", "Chat", "Clock", "Terminal", "Test")

# Windows
Window = ttk.PanedWindow(Emilion, orient = HORIZONTAL)
Window.place(x = 0 , y = 0, width = 1000 , height = 1000)

# Frames
FrameLeft = Frame(Window, bg = "cyan", relief = "ridge") # Ice Window
Window.add(FrameLeft, weight = 2) # Start position of Slider

FrameRight = Frame(Window, bg = "red", relief = "ridge") # Fire Window
Window.add(FrameRight, weight = 30)

# Draw Ice Menu
Distance = 0
ButtonIcons = []
for i in range(len(Icons)): # Go through list of Icons and place with Run command from Helper class
    ButtonIcons.append(Button(FrameLeft, text = Icons[i], relief = "ridge", font = ("", 10), command = lambda x = i:Helper.Run(x)))
    ButtonIcons[i].place(x = 0, y = Distance, width = 64, height = 32) # Place under each other
    Distance += 32

# Loop
Emilion.minsize(500, 500)
Emilion.mainloop()
