
from tkinter import *

root = Tk()
root.resizable(0, 0)
root.title('QUIZ')

#constants
BG_COLOR = '#fdfdfd'
QUESTION_TEXT_COLOR = '#cabbe9'
OPTIONS_COLOR = '#086972'

canvas = Canvas(root, width=1500, height=500, bg=BG_COLOR)
canvas.pack()
class Question():
    def question_first(self):
        self.text = canvas.create_text(120, 250, text="2 + 2 =", justify=CENTER,  font="Arial 40", fill=QUESTION_TEXT_COLOR)
        self.line = canvas.create_line(500, 0, 500 ,520, fill='black')

    def question_second(self):
        self.text = canvas.create_text(620, 250, text="2 * 3 =", justify=CENTER,  font="Arial 40", fill=QUESTION_TEXT_COLOR)
        self.line = canvas.create_line(1000, 0, 1000 , 1020, fill='black')

    def question_third(self):
        self.text = canvas.create_text(1120, 250, text='-12 + 1 =', justify=CENTER,  font="Arial 40", fill=QUESTION_TEXT_COLOR)

class Options():
    def __init__(self):
        self.x = 5
        self.y = 5
        self.size = 24
        self.canvas = canvas
        questions_and_answers = {
            '2 + 2': '4',
            '2 * 3': '6',
            '-12 + 1': '-11'
        }
        questions = questions_and_answers.values()
        answers = questions_and_answers.keys()

    def click_event(self):
        pass
    
    def option_first_of_first_drill(self):    
        self.option_first = canvas.create_text(350, 150, text="5", justify=CENTER,  font="Arial 27", fill=OPTIONS_COLOR)
        self.circle = canvas.create_oval(self.x, self.y, self.size, self.size, command=self.click_event()) #Тут self.
        self.canvas.move(self.circle, 305, 135)
    
    def option_second_of_first_drill(self):
        self.option_second = canvas.create_text(350, 350, text="4", justify=CENTER,  font="Arial 27", fill=OPTIONS_COLOR)
        self.circle = canvas.create_oval(self.x, self.y, self.size, self.size,)
        self.canvas.move(self.circle, 305, 335)
    
    def option_first_of_second_drill(self):    
        self.option_first = canvas.create_text(950, 150, text="6", justify=CENTER,  font="Arial 27", fill=OPTIONS_COLOR)
        self.circle = canvas.create_oval(self.x, self.y, self.size, self.size, command=self.click_event()) #Тут self.
        self.canvas.move(self.circle, 905, 135)
    
    def option_second_of_second_drill(self):
        self.option_second = canvas.create_text(950, 350, text="7", justify=CENTER,  font="Arial 27", fill=OPTIONS_COLOR)
        self.circle = canvas.create_oval(self.x, self.y, self.size, self.size,)
        self.canvas.move(self.circle, 905, 335)

    def option_first_of_third_drill(self):    
        self.option_first = canvas.create_text(1450, 150, text="-13", justify=CENTER,  font="Arial 27", fill=OPTIONS_COLOR)
        self.circle = canvas.create_oval(self.x, self.y, self.size, self.size, command=self.click_event()) #Тут self.
        self.canvas.move(self.circle, 1385, 137)
    
    def option_second_of_third_drill(self):
        self.option_second = canvas.create_text(1450, 350, text="-11", justify=CENTER,  font="Arial 27", fill=OPTIONS_COLOR)
        self.circle = canvas.create_oval(self.x, self.y, self.size, self.size,)
        self.canvas.move(self.circle, 1385, 337)

#classes
o = Options()
q = Question()

#functions
q.question_first()
q.question_second()
q.question_third()
#options
o.option_first_of_first_drill()
o.option_second_of_first_drill()
o.option_first_of_second_drill()
o.option_second_of_second_drill()
o.option_first_of_third_drill()
o.option_second_of_third_drill()



root.mainloop()