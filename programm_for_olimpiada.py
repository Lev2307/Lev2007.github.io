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
canvas = Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE, bg='#97a98b')
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
        self.canvas.delete(0, ALL)
        Student()

    def delete_all_teacher(self):
        self.btn_teacher.destroy()
        self.btn_student.destroy()
        Teacher()



class Student():
    def __init__(self):
        self.canvas = canvas
        self.entry_field = Entry(self.canvas, width=30)
        self.entry_field.place(x=100, y=200)
        self.btn_answer = Button(self.canvas, width=10, height=2, text='Ответ: ', command=self.send_guess)
        self.btn_answer.place(x=160, y=250)
        self.true_answers = 1
        self.questions = list(q_and_a.keys())
        self.answers = list(q_and_a.values())
        self.mark_q = len(q_and_a) - 1
        self.printed_form()
    
    def printed_form(self):
        if self.mark_q == -1:
            self.end()
        try:
            self.text_math.destroy()
        except:
            pass
        self.printed_text = f'{self.questions[self.mark_q]}'
        self.text_math = Label(canvas, text=f'{self.printed_text}', bg='#97a98b', fg='black', font='Arial 15')
        self.text_math.place(x=180, y=170)
        self.mark_q -= 1
        if self.mark_q == -2:
            self.text_math.destroy()
    
    def send_guess(self):
        self.user_guess = self.entry_field.get()
        self.entry_field.delete(0 , END)
        self.printed_form()
        self.check_true_answer()

    def check_true_answer(self):
        if int(self.user_guess) == int(self.answers[self.mark_q + 2]):
            self.true_answers += 1
    
    def end(self):
        self.btn_answer.destroy()
        self.entry_field.destroy()
        self.canvas.delete(0, ALL)
        self.text = self.canvas.create_text(200, 200, text=f"Правильных ответов: {self.true_answers}", justify=CENTER,  font="Arial 20", fill='black')

class Teacher():
    def __init__(self):
        self.canvas = canvas
        self.text = self.canvas.create_text(200, 150, text="Напишите пример: ", font="Arial 15", fill='black')
        self.entry_field = Entry(self.canvas, width=30)
        self.entry_field.place(x=100, y=200)
        self.btn_answer = Button(self.canvas, width=10, height=2, text='Отправить: ', command=self.send_question)
        self.btn_answer.place(x=160, y=250)
        self.btn_exit = Button(self.canvas, width=6, height=1, text='Выйти', bg='red', command=self.go_to_menu)
        self.btn_exit.place(x=175, y=350)
        self.questions = list(q_and_a.keys())

    def send_question(self):
        self.user_question = self.entry_field.get()
        self.entry_field.delete(0, END)
        self.questions.append(self.user_question)
        self.change_dictionary()
    
    def change_dictionary(self):
        q_and_a[self.user_question] = eval(f'{self.user_question}')

    def go_to_menu(self):
        self.entry_field.destroy()
        self.btn_answer.destroy()
        self.btn_exit.destroy()
        self.canvas.delete(0, ALL)
        Board()
        
b = Board()
master.mainloop()