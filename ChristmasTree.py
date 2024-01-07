from tkinter import *

window = Tk()

canvas = Canvas(window, width=500, height=500)
canvas.pack()
tree = canvas.create_polygon(197, 177, 107, 397, 287, 397, fill="green", outline="black", width=3)
star = canvas.create_polygon(196, 100, 177, 148, 118, 164, 167, 185, 144, 240, 196, 206, 249, 240, 225, 185, 274, 164, 216, 148, fill="yellow", outline="black", width=3)
branch = canvas.create_rectangle(177, 397, 217, 500, fill="brown", outline="black", width=3)
window.mainloop()