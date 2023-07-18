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

# Icons

Icons = ("Home", "Storage", "Calculator", "Test")

# Windows
Window = ttk.PanedWindow(Emilion, orient=VERTICAL)
Window.place(x = 0, y = 0, width = Widht, height = Height)

# Frames
Frame = Frame(Window, relief = "ridge")
Window.add(Frame, weight = 1)

# Draw Menu
Distance = 0
ButtonIcons = []
for i in range(len(Icons)):
    ButtonIcons.append(Button(Frame, text = Icons[i], relief = "ridge", font = ("", 10)))
    ButtonIcons[i].place(x = Distance, y = 0, width = 32, height = 32)
    Distance += 32

# Loop
mainloop()
