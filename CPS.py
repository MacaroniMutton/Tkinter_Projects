import sys
from tkinter import *
import time

seconds = [5, 10, 15, 20]
count = 0

def counting(event):
    global count
    count += 1
    clicks.set(count)

def results():    
    timerLabel.pack_forget()
    clicksLabel.pack_forget()
    clickFrame.pack_forget()
    resultFrame.pack(expand=True, fill="both")
    cpsValue = clicks.get() / seconds[x.get()]
    cps.set("Clicks Per Second : {0:.2f}".format(cpsValue))

def timeTicking():
    if timer.get()==1:
        window.unbind("<Button-1>")
        
        results()
    else:
        timer.set(timer.get()-1)
        clicks.set(count)
        timerLabel.pack(side=TOP)
        clicksLabel.pack(anchor=S, pady=30)
        window.bind("<Button-1>", counting)
        window.after(1000, timeTicking)
        


def startClick():
    countdownLabel.config(font=("Helvetica, 20"))
    countdown.set("Start Clicking!!")
    timer.set(seconds[x.get()]+1)
    timeTicking()

def updateCountdown(i):
    if(i==0):
        startClick()
    else:
        countdown.set(f"{i}")
        window.after(1000, updateCountdown, i-1)

def start():
    startFrame.pack_forget()
    clickFrame.pack(expand=True, fill="both")
    updateCountdown(3)

def tryAgain():
    global count
    resultFrame.pack_forget()
    count = 0
    startFrame.pack(expand=True, fill="both")


window = Tk()
window.geometry("800x500")
window.title("CPS")
window.wm_attributes('-toolwindow', 'True')

x = IntVar()
countdown = StringVar()
timer = IntVar()
clicks = IntVar()
cps = StringVar()

startFrame = Frame(window)
startFrame.pack(expand=True, fill="both")

title = Label(startFrame,
              text="Clicks per Second Test",
              font=("Helvetica", 20, "bold"))
title.pack()

choice = Label(startFrame,
               text="How many seconds do you want to go? : ",
               font=("Comic Sans", 13))
choice.pack(anchor=W, pady=10)

for i in range(len(seconds)):
    radiobtn = Radiobutton(startFrame, 
                           text=f"{seconds[i]} seconds", 
                           variable=x, 
                           value=i, 
                           indicatoron=False, 
                           width=360, 
                           font=("Arial, 16"), 
                           fg="yellow", 
                           bg="gray", 
                           relief=RAISED, 
                           bd=5,
                           activebackground="#8db598",
                           selectcolor="#8db598")
    radiobtn.pack(anchor=CENTER)

startbtn = Button(startFrame, text="Start", font=("Comic Sans", 16), command=start)
startbtn.pack(anchor=CENTER, pady=40)

clickFrame = Frame(window)

countdownLabel = Label(clickFrame,
                       textvariable=countdown,
                       font=("Helvetica", 40, "bold"))
countdownLabel.pack(anchor=CENTER, expand=True)

timerLabel = Label(clickFrame,
                   textvariable=timer,
                   font=("Helvetica", 15, "bold"))

clicksLabel = Label(clickFrame,
                    textvariable=clicks,
                    font=("Helvetica", 15, "bold"))

resultFrame = Frame(window)

CPSLabel = Label(resultFrame,
                       textvariable=cps,
                       font=("Helvetica", 40, "bold"))
CPSLabel.pack(anchor=CENTER, expand=True)

tryAgainbtn = Button(resultFrame,
                     text="Try Again?",
                     font=("Helvetica", 15, "bold"),
                     command=tryAgain)
tryAgainbtn.pack(pady=40)

exitbtn = Button(resultFrame,
                 text="Exit",
                 font=("Helvetica", 15, "bold"),
                 command=sys.exit)
exitbtn.pack(pady=40)


window.mainloop()