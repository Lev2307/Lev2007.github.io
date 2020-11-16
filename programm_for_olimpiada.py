from tkinter import *

root = Tk()
root.resizable(0, 0)
root.title('QUIZ')

#constants
BG_COLOR = '#fdfdfd'
QUESTION_TEXT_COLOR = '#cabbe9'
OPTIONS_COLOR = '#086972'

canvas = Canvas(root, width=500, height=500, bg=BG_COLOR)
canvas.pack()
class Question():
    def quest(self):
        self.text = canvas.create_text(120, 250, text="2 + 2 =", justify=CENTER,  font="Arial 40", fill=QUESTION_TEXT_COLOR)

class Options():
    def __init__(self):
        self.x = 5
        self.y = 5
        self.size = 24
        self.canvas = canvas

    def option_first(self):
        def click_event(self):
            pass
        self.option_first = canvas.create_text(350, 150, text="5", justify=CENTER,  font="Arial 27", fill=OPTIONS_COLOR)
        self.circle = canvas.create_oval(self.x, self.y, self.size, self.size, command=click_event(1))
        self.canvas.move(self.circle, 305, 135)
    
    def option_second(self):
        self.option_second = canvas.create_text(350, 350, text="4", justify=CENTER,  font="Arial 27", fill=OPTIONS_COLOR)
        self.circle = canvas.create_oval(self.x, self.y, self.size, self.size,)
        self.canvas.move(self.circle, 305, 335)

#classes
o = Options()
q = Question()

#functions
q.quest()
o.option_first()
o.option_second()




root.mainloop()