import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
t = turtle.Turtle()
t.speed(8)
t.pensize(3)

def draw_leg(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("darkgreen")
    t.begin_fill()
    t.circle(25) 
    t.end_fill()

draw_leg(-50, -30)
draw_leg(50, -30)
draw_leg(-95, 70)
draw_leg(95, 70)

t.penup()
t.goto(-0, 00)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.circle(100)
t.end_fill()

t.pencolor("lightgreen")
for _ in range(6):
    t.penup()
    t.goto(0, 90)
    t.pendown()
    t.circle(40)
    t.right(60)

t.penup()
t.goto(10, 170)
t.pendown()
t.fillcolor("darkgreen")
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(-10, 220)
t.dot(10, "white")
t.dot(5, "black") 
t.penup()
t.goto(10, 220)
t.dot(10, "white")
t.dot(5, "black")

t.hideturtle()
turtle.done()
