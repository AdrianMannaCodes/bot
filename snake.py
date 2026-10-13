import tkinter as t
import random as r

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

class Tile: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

window = t.Tk()
window.title("スネイク")
window.resizable(False, False)

canvas = t.Canvas(window, bg="teal", 
                  width=WINDOW_HEIGHT, 
                  height=WINDOW_HEIGHT,
                  borderwidth=0,
                  highlightthickness=0)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width=window.winfo_screenmmwidth()
screen_height=window.winfo_screenmmheight()

window_x = int(screen_width/2-window_width/2)
window_y = int(screen_height/2-screen_height/2)

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

snake = Tile(125, 125)
food = Tile(250, 250)
vX = 0
vY = 0

def change_direction(e):
    global vX, vY

    if e.keysym == "w" and vY!=1:
        vX=0
        vY=-1
    elif e.keysym=="s" and vY != -1:
        vX=0
        vY=1
    elif e.keysym=="a" and vX!=1:
        vX=-1
        vY =0
    elif e.keysym=="d" and vX!=-1:
        vX=1
        vY=0
    
def move():
    global snake

    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y))
        food.x = r.randint(0, COLS-1) * TILE_SIZE
    snake.x += vX * TILE_SIZE
    snake.y += vY * TILE_SIZE
def draw():
    global snake
    move()

    canvas.delete("all")

    canvas.create_rectangle(food.x, food.y, food.x+25, food.y+25, fill='#ff0000')

    canvas.create_rectangle(snake.x, snake.y, snake.x+TILE_SIZE, snake.y+TILE_SIZE, fill="#00ff00")

    window.after(100, draw)

draw()

window.bind("<KeyRelease>", change_direction)
window.mainloop()