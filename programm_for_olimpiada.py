from tkinter import *

master = Tk()
master.resizable(0, 0)
master.geometry("400x400")
master.title('OLIMPICS OF PYTHON')

# constants
CANVAS_SIZE = 400

q_and_a = {
    '8+8': '16',
    '2-2': '0',
    '3+3': '6'
}
canvas = Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE, bg='#a3907e')
canvas.pack()


class Board():
    def __init__(self):
        self.canvas = canvas
        self.btn_teacher = Button(self.canvas, padx=13.5, pady=20, width=15, height=5, text='Учитель', bg='#713045', fg='white', command=self.delete_all_teacher)
        self.btn_student = Button(self.canvas , padx=13.5, pady=20, width=15, height=5, text='Ученик', bg='#1e6262', fg='white', command=self.delete_all_student)
        self.btn_teacher.place(x=50, y=160)
        self.btn_student.place(x=220, y=160)

    def delete_all_student(self):
        self.btn_teacher.destroy()
        self.btn_student.destroy()
        Student()

    def delete_all_teacher(self):
        self.btn_teacher.destroy()
        self.btn_student.destroy()
        self.teachers_page()

    # def students_page(self):
    #     self.first_question()


class Student(Board):
    def __init__(self):
        self.canvas = canvas
        self.entry = Entry(self.canvas, width=30, borderwidth=3)
        self.entry.place(x=100, y=200)
        self.btn_answer = Button(self.canvas, width=10, height=2, text='Ответ: ')
        self.btn_answer.place(x=160, y=250)
        self.questions = q_and_a.keys()
        self.answers = q_and_a.values()
    
    def printed_form():
        pass

b = Board()
master.mainloop()