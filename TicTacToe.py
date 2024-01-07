from tkinter import *
import random
import sys
import time

over = False
player = "X"
computer = True
options = ["Computer", "Human"]

def playAgain():
    global board
    titleFrame.pack_forget()
    playFrame.pack_forget()
    startFrame.pack(expand=True, fill="both")
    playAgainbtn.pack_forget()
    exitbtn.pack_forget()

def check(player):
    global over
    noMore = True
    for row in board:
        for value in row:
            if value.get()=="":
                noMore = False
    if noMore:
        over = True
        result.config(text="It is a Tie!")
    print(board)
    if board[0][0].get()==board[0][1].get()==board[0][2].get()=="X" or board[1][0].get()==board[1][1].get()==board[1][2].get()=="X" or board[2][0].get()==board[2][1].get()==board[2][2].get()=="X" or board[0][0].get()==board[1][1].get()==board[2][2].get()=="X" or board[0][2].get()==board[1][1].get()==board[2][0].get()=="X" or board[0][0].get()==board[1][0].get()==board[2][0].get()=="X" or board[0][1].get()==board[1][1].get()==board[2][1].get()=="X" or board[0][2].get()==board[1][2].get()==board[2][2].get()=="X":
        over = True
        result.config(text="Player 1 Won!")
    if board[0][0].get()==board[0][1].get()==board[0][2].get()=="O" or board[1][0].get()==board[1][1].get()==board[1][2].get()=="O" or board[2][0].get()==board[2][1].get()==board[2][2].get()=="O" or board[0][0].get()==board[1][1].get()==board[2][2].get()=="O" or board[0][2].get()==board[1][1].get()==board[2][0].get()=="O" or board[0][0].get()==board[1][0].get()==board[2][0].get()=="O" or board[0][1].get()==board[1][1].get()==board[2][1].get()=="O" or board[0][2].get()==board[1][2].get()==board[2][2].get()=="O":
        over = True
        result.config(text="Player 2 Won!")


def play(event, var):
    global over, board, boxes, player
    if computer:
        event.widget.unbind("<Button-1>")
        var.set(player)
        result.config(text=f"Player 1's Turn")
        check("Player")
        if not over:
            result.config(text="Player 2's Turn")
            window.update()
            time.sleep(0.8)
            compVar = StringVar()
            compVar.set("O")
            box = None
            while compVar.get()!="":
                i = random.randint(0,2)
                j = random.randint(0,2)
                compVar = board[i][j]
                box = boxes[i][j]
            compVar.set("O")
            box.unbind("<Button-1>")
            result.config(text="Player 1's Turn")
            check("Computer")
        if over:
            unlisten()
            playAgainbtn.pack()
            exitbtn.pack()
    else:
        if not over:
            event.widget.unbind("<Button-1>")
            var.set(player)
            if player=="X":
                player = "O"
                result.config(text=f"Player 2's Turn")
            else:
                player = "X"
                result.config(text=f"Player 1's Turn")
            check("Player")
        if over:
            unlisten()
            playAgainbtn.pack()
            exitbtn.pack()

def listen():
    global boxes, board
    boxes[0][0].bind("<Button-1>", lambda event: play(event, board[0][0]))
    boxes[0][1].bind("<Button-1>", lambda event: play(event, board[0][1]))
    boxes[0][2].bind("<Button-1>", lambda event: play(event, board[0][2]))
    boxes[1][0].bind("<Button-1>", lambda event: play(event, board[1][0]))
    boxes[1][1].bind("<Button-1>", lambda event: play(event, board[1][1]))
    boxes[1][2].bind("<Button-1>", lambda event: play(event, board[1][2]))
    boxes[2][0].bind("<Button-1>", lambda event: play(event, board[2][0]))
    boxes[2][1].bind("<Button-1>", lambda event: play(event, board[2][1]))
    boxes[2][2].bind("<Button-1>", lambda event: play(event, board[2][2]))

def unlisten():
    global boxes, board
    boxes[0][0].unbind("<Button-1>")
    boxes[0][1].unbind("<Button-1>")
    boxes[0][2].unbind("<Button-1>")
    boxes[1][0].unbind("<Button-1>")
    boxes[1][1].unbind("<Button-1>")
    boxes[1][2].unbind("<Button-1>")
    boxes[2][0].unbind("<Button-1>")
    boxes[2][1].unbind("<Button-1>")
    boxes[2][2].unbind("<Button-1>")

def start():
    global computer, over, player
    player = "X"
    startFrame.pack_forget()
    if x.get()==1:
        computer = False
    if x.get()==0:
        computer = True
    result.config(text="Player 1's Turn")
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j].set("")
    listen()
    over = False
    titleFrame.pack(anchor=N, pady=50)
    playFrame.pack(anchor=CENTER, expand=True)




window = Tk()
window.geometry("420x420")
window.title("Tic-Tac-Toe")

board = [[StringVar() for _ in range(3)] for _ in range(3)]
x = IntVar()

startFrame = Frame(window)
startFrame.pack(expand=True, fill="both")

title = Label(startFrame,
              text="Tic Tac Toe",
              font=("Helvetica", 20, "bold"))
title.pack()

choice = Label(startFrame,
               text="Who is player 2?",
               font=("Comic Sans", 13))
choice.pack(anchor=W, pady=10)

for i in range(len(options)):
    radiobtn = Radiobutton(startFrame, 
                           text=options[i], 
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


titleFrame = Frame(window)
# titleFrame.pack(anchor=N, pady=50)

result = Label(titleFrame, text="Player 1's Turn", font=("Cursive", 20), fg="blue")
result.pack()

playAgainbtn = Button(titleFrame, text="New Game", command=playAgain)

exitbtn = Button(titleFrame, text="Exit", command=sys.exit)

playFrame = Frame(window)
# playFrame.pack(anchor=CENTER, expand=True)



TL = Label(playFrame, textvariable=board[0][0],bg="red", width=8, height=4, relief=SOLID, bd=2)
TM = Label(playFrame, textvariable=board[0][1],bg="red", width=8, height=4, relief=SOLID, bd=2)
TR = Label(playFrame, textvariable=board[0][2],bg="red", width=8, height=4, relief=SOLID, bd=2)
ML = Label(playFrame, textvariable=board[1][0],bg="red", width=8, height=4, relief=SOLID, bd=2)
MM = Label(playFrame, textvariable=board[1][1],bg="red", width=8, height=4, relief=SOLID, bd=2)
MR = Label(playFrame, textvariable=board[1][2],bg="red", width=8, height=4, relief=SOLID, bd=2)
BL = Label(playFrame, textvariable=board[2][0],bg="red", width=8, height=4, relief=SOLID, bd=2)
BM = Label(playFrame, textvariable=board[2][1],bg="red", width=8, height=4, relief=SOLID, bd=2)
BR = Label(playFrame, textvariable=board[2][2],bg="red", width=8, height=4, relief=SOLID, bd=2)

boxes = [[TL, TM, TR], 
         [ML, MM, MR], 
         [BL, BM, BR]]

for i in range(len(boxes)):
    for j in range(len(boxes[0])):
        boxes[i][j].grid(row=i, column=j)

# listen()


window.mainloop()