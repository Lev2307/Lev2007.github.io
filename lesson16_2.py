from tkinter import *
from time import sleep

root = Tk()

canvas = Canvas(root, width=520, height=520, bg='#eac100')
canvas.pack()

class Circle():
    def __init__(self):
        self.x = 5
        self.y = 5
        self.size = 16
        self.speed_x = 15
        self.speed_y = 20
        self.canvas_size = 520
        self.wall_width = 100
        self.object = canvas.create_oval(self.x, self.y, self.size, self.size, fill='#0b8457')
        self.canvas = canvas
        self.canvas.move(self.object, 120, 120)

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

    def getter_status(self):
        pos_circle = canvas.coords(self.object)
        if pos_circle[3] >= self.canvas_size:
            canvas.delete(ALL)
            canvas.create_text(280, 260, text="YOU LOSE =( ", justify=CENTER,  font="Arial 30", fill='#3e3636')
            return False
        else:
            return True

    def check_collision_with_platform(self):
        pos_platform = p.getter_coords()
        pos_circle = canvas.coords(self.object)
        if pos_circle[3] >= pos_platform[1] and pos_circle[2] >= pos_platform[0] and pos_circle[0] <= pos_platform[2] and pos_circle[1] <= pos_platform[3]:
            self.speed_y *= -1

class Platform(Circle):
    def __init__(self):
        self.x = 0
        self.canvas = canvas
        self.canvas_size = 520
        self.object = canvas.create_rectangle(0, 0 , 100, 10, fill='#10316b')
        self.canvas.move(self.object, 370, 450)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, event):
        pos = self.canvas.coords(self.object)
        if event.keysym == 'Left' and pos[0] > 0:
            canvas.move(self.object, -10, 0)

    def turn_right(self, event):
        pos = self.canvas.coords(self.object)
        if event.keysym == 'Right' and pos[2] < self.canvas_size:
            canvas.move(self.object, 10, 0)

    def check_collision(self):
        pos = canvas.coords(self.object)
        if pos[0] <= 0:
            canvas.move(self.object, 10, 0)
        elif pos[2] >= self.canvas_size:
            canvas.move(self.object, -10, 0)

    def getter_coords(self):
        posp = canvas.coords(self.object)
        return posp

class Wall(Circle):
    def __init__(self):
        self.canvas = canvas
    def create_wall(self):
        for _ in range(100):
            self.square = self.canvas.create_rectangle(2, 2, 15, 15, fill='#dee1ec')
            



w = Wall()
p = Platform()
c1 = Circle()
root.title('Game')

while c1.getter_status():
    c1.check_collision_with_platform()
    w.create_wall()
    c1.move()
    root.update()
    sleep(0.02)

root.mainloop()