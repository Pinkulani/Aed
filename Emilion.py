from tkinter import *
from tkinter import ttk

# Setup
Height = "1000"
Widht = "1000"

Emilion = Tk()
Emilion.title("Emilion 🥕")
Emilion.geometry("1000x1000")

Style = ttk.Style()
Style.theme_use("clam")

# Icons
Icons = ("Home", "Storage", "Calculator", "Timer", "Notes", "Contacts", "Chat", "Terminal", "Test")

# Windows
Window = ttk.PanedWindow(Emilion, orient = HORIZONTAL)
Window.place(x = 0 , y = 0, width = 1000 , height = 1000)

# Frames
FrameLeft = Frame(Window, bg = "blue", relief = "ridge") # Ice Window
Window.add(FrameLeft, weight = 5) # Start position of Slider

FrameRight = Frame(Window, bg = "red", relief = "ridge") # Fire Window
Window.add(FrameRight, weight = 30)

# Draw Ice Menu
Distance = 0
ButtonIcons = []
for i in range(len(Icons)):
    ButtonIcons.append(Button(FrameLeft, text = Icons[i], relief = "ridge", font = ("", 10)))
    ButtonIcons[i].place(x = 0, y = Distance, width = 64, height = 32)
    Distance += 32

# Loop
Emilion.minsize(500, 500)
Emilion.mainloop()
