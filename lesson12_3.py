import turtle

screen = turtle.getscreen()
t = turtle.Turtle()
for _ in range(6):
    t.forward(100)
    t.left(90)

t.goto(60,100)
screen.mainloop()