from tkinter import *
import random
import time

BACKGROUND_COLOR = "#000000"
SNAKE_COLOR = "#00FF00"
SNAKE_BORDER_COLOR = "#FFFFFF"
FOOD_COLOR = "#FF0000"
GAME_WIDTH = 700
GAME_HEIGHT = 700
CELL_SIZE = 50
START_X = 0
START_Y = 0
START_BODY_PARTS = 3
SPEED = 100


class Snake:
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.body_parts = START_BODY_PARTS
        self.coordinates = []
        self.squares = []
        for square in range(self.body_parts):
            square = self.canvas.create_rectangle(START_X, START_Y, START_X + CELL_SIZE, START_Y + CELL_SIZE, fill=SNAKE_COLOR, outline=SNAKE_BORDER_COLOR, width=2)
            self.squares.append(square)
            self.coordinates.append([START_X, START_Y])

    def addSquare(self, x, y):
        newSquare = self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=SNAKE_COLOR, outline=SNAKE_BORDER_COLOR, width=2)
        self.coordinates.insert(0, [x, y])
        self.squares.insert(0, newSquare)

    def removeSquare(self):
        self.coordinates.pop()
        self.canvas.delete(self.squares[-1])
        self.squares.pop()


class Food:
    
    def __init__(self, canvas):
        self.canvas = canvas
        noOfTilesX = GAME_WIDTH / CELL_SIZE
        noOfTilesY = GAME_HEIGHT / CELL_SIZE
        x = random.randint(0, noOfTilesX-1) * CELL_SIZE
        y = random.randint(0, noOfTilesY-1) * CELL_SIZE
        self.coordinates = [x, y]
        self.canvas.create_oval(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=FOOD_COLOR, tag="food")
    
    def respawn_food(self):
        self.canvas.delete("food")
        self = Food(self.canvas)
        return self

def next_turn(food, snake):
    global direction, score, running

    [x, y] = snake.coordinates[0]
    
    if direction=="up":
        y -= CELL_SIZE
    elif direction=="down":
        y += CELL_SIZE
    elif direction=="left":
        x -= CELL_SIZE
    elif direction=="right":
        x += CELL_SIZE

    snake.addSquare(x, y)
    if x==food.coordinates[0] and y==food.coordinates[1]:
        score += 1
        scoreLabel.config(text=f"Score : {score}")
        food = food.respawn_food()
    else:
        snake.removeSquare()
    
    check_collisions(snake)

    if running:
        window.after(SPEED, lambda: next_turn(food, snake))

def change_direction(event, new_direction):
    global direction

    if new_direction=="up":
        if direction!="down":
            direction = new_direction
    elif new_direction=="down":
        if direction!="up":
            direction = new_direction
    elif new_direction=="left":
        if direction!="right":
            direction = new_direction
    elif new_direction=="right":
        if direction!="left":
            direction = new_direction

def game_over():
    global score
    scoreLabel.config(text=f"Score : {score} \nGAME OVER")
    return False

def check_collisions(snake):
    global running

    [x, y] = snake.coordinates[0]

    if x<0 or x>=GAME_WIDTH:
        running = game_over()
    elif y<0 or y>=GAME_HEIGHT:
        running = game_over()

    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1]:
            running = game_over()

def menu():
    pass

def settings():
    pass

window = Tk()
window.title("Snake Game")



playFrame = Frame(window)
playFrame.pack()

score = 0
direction = "down"
running = True

scoreLabel = Label(playFrame, text=f"Score : {score}", font=("Helvetica", 20))
scoreLabel.pack()

canvas = Canvas(playFrame, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

food = Food(canvas)
snake = Snake(canvas)

next_turn(food, snake)

window.bind("<w>", lambda event: change_direction(event, "up"))
window.bind("<a>", lambda event: change_direction(event, "left"))
window.bind("<s>", lambda event: change_direction(event, "down"))
window.bind("<d>", lambda event: change_direction(event, "right"))
window.bind("<Up>", lambda event: change_direction(event, "up"))
window.bind("<Left>", lambda event: change_direction(event, "left"))
window.bind("<Down>", lambda event: change_direction(event, "down"))
window.bind("<Right>", lambda event: change_direction(event, "right"))

window.update()

w = window.winfo_width()
h = window.winfo_height()

# get screen width and height
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = int((ws/2) - (w/2))
y = int((hs/2) - (h/2)) - 30

# set the dimensions of the screen 
# and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.mainloop()