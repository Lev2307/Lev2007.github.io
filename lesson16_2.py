from tkinter import *
from time import sleep

root = Tk()

canvas = Canvas(root, width=500, height=500, bg='wheat')
canvas.pack()

class Circle():
    def __init__(self):
        self.x = 10
        self.y = 10
        self.size = 25
        self.speed_x = 3
        self.speed_y = 2
        self.canvas_size = 500
        self.wall_width = 100
        self.object = canvas.create_oval(self.x, self.y, self.size, self.size, fill='red')

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        canvas.move(self.object, self.speed_x, self.speed_y)
        self.check_collision()

    def check_collision(self):
        pos = canvas.coords(self.object)
        if pos[0] <= 0:
            self.speed_x *= -1
        elif pos[1] <= 0:
            self.speed_y *= -1
        elif pos[2] >= self.canvas_size:
            self.speed_x *= -1
        elif pos[3] >= self.canvas_size:
            self.speed_y *= -1

    def check_collision_with_wall():
        pos = canvas.coords(self.object)
        if pos[0] <= 0:
            self.speed_x *= -1
        elif pos[1] <= 0:
            self.speed_y *= -1
        elif pos[2] >= self.wall_width:
            self.speed_x *= -1
        elif pos[3] >= self.wall_width:
            self.speed_y *= -1


class Wall():
    def __init__(self):
        self.x = 0
        self.canvas = canvas
        self.canvas_size = 500
        self.object = canvas.create_rectangle(0, 0 , 100, 10, fill='blue')
        self.canvas.move(self.object, 200, 330)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, event):
        if event.keysym == 'Left':
            canvas.move(self.object, -10, 0)

    def turn_right(self, event):
        if event.keysym == 'Right':
            canvas.move(self.object, 10, 0)

    def check_position_in_canvas(self):
        pos_wall = canvas.coords(self.object)
        if pos_wall[0] < self.canvas_size:
            canvas.bind_all('<KeyPress-Left>', self.turn_left) = False
        elif pos_wall[0] < self.canvas_size:
            canvas.bind_all('<KeyPress-Right>', self.turn_right) = False

w = Wall()
c1 = Circle()

while True:
    c1.move()
    root.update()
    sleep(0.03)

root.mainloop()