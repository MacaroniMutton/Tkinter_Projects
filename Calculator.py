from tkinter import *

def buttonPress(num):
    expression.set(expression.get()+str(num))

def evaluate():
    try:
        result.set(str(eval(expression.get())))
    except Exception:
        result.set("ERROR")

def clear():
    expression.set("")
    result.set("")

def backspace():
    result.set("")
    expression.set(expression.get()[:-1])

window = Tk()
window.geometry("420x500")
window.title("Calculator")

expression = StringVar()
result = StringVar()

screen = Frame(window,
               bg="white")
screen.pack()

evaluateScreen = Label(screen,
               textvariable=expression,
               width=40,
               bg="white")
evaluateScreen.pack(anchor=N, pady=20)

resultScreen = Label(screen,
               textvariable=result,
               width=40,
               bg="white")
resultScreen.pack()

buttonFrame = Frame(window)
buttonFrame.pack()

button_1 = Button(buttonFrame,bg="gray", width=6, height=3, text="1", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress(1))


button_2 = Button(buttonFrame,bg="gray", width=6, height=3, text="2", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress(2))


button_3 = Button(buttonFrame,bg="gray", width=6, height=3, text="3", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress(3))


button_4 = Button(buttonFrame,bg="gray", width=6, height=3, text="4", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress(4))


button_5 = Button(buttonFrame,bg="gray", width=6, height=3, text="5", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress(5))


button_6 = Button(buttonFrame,bg="gray", width=6, height=3, text="6", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress(6))


button_7 = Button(buttonFrame,bg="gray", width=6, height=3, text="7", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress(7))


button_8 = Button(buttonFrame,bg="gray", width=6, height=3, text="8", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress(8))


button_9 = Button(buttonFrame,bg="gray", width=6, height=3, text="9", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress(9))


button_0 = Button(buttonFrame,bg="gray", width=6, height=3, text="0", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress(0))


button_add = Button(buttonFrame,bg="gray", width=6, height=3, text="+", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress("+"))


button_sub = Button(buttonFrame,bg="gray", width=6, height=3, text="-", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress("-"))


button_mul = Button(buttonFrame,bg="gray", width=6, height=3, text="*", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress("*"))


button_div = Button(buttonFrame,bg="gray", width=6, height=3, text="/", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress("/"))


button_dot = Button(buttonFrame,bg="gray", width=6, height=3, text=".", relief=RAISED, bd=2, activebackground="gray", command=lambda: buttonPress("."))


button_eval = Button(buttonFrame,bg="gray", width=6, height=3, text="=", relief=RAISED, bd=2, activebackground="gray", command=evaluate)


button_clear = Button(buttonFrame,bg="gray", width=6, height=3, text="C", relief=RAISED, bd=2, activebackground="gray", command=clear)


button_back = Button(buttonFrame,bg="gray", width=6, height=3, text="Back", relief=RAISED, bd=2, activebackground="gray", command=backspace)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4, column=1)
button_add.grid(row=3, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=1, column=3)
button_div.grid(row=0, column=3)
button_dot.grid(row=4, column=2)
button_eval.grid(row=4, column=3)
button_back.grid(row=0, column=1)
button_clear.grid(row=0, column=0)

window.mainloop()