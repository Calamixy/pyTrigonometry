from tkinter import Tk, Canvas
import math

canvas_width = 500
canvas_height = 500

master = Tk()
master.winfo_toplevel().title("calamixy's trigonometry stuff")
myCanvas = Canvas(master)
myCanvas.pack()

def dot(x, y, r): # x, y are the position of the dot and r is the radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return myCanvas.create_oval(x0, y0, x1, y1, fill="pink")

for x in range(51):
    _x = 5 + 5 * math.sin(x)
    _y = 5 + 5 * math.cos(x)

    good_pi = math.pi * 2

    print(_x + 5 * math.sin(x), _y + 5 * math.cos(x), 0)
    dot(_x / 20 * good_pi * 10 + 30, _y / 20 * good_pi * 10 + 30, 1)

master.mainloop()