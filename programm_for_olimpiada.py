from tkinter import *

master = Tk()
master.resizable(0,0)
master.title('OLIMPICS OF PYTHON')

first_answer = {'-3 + 3': '0'}
second_answer = {'7 * 2': '14'}
third_answer = {'0 + 1' : '1'}
answers = []
first_answer_k = first_answer.values()
second_answer_k = second_answer.values()
third_answer_k = third_answer.values()

def first_text():
    text = Label(master, text="Вам осталось ответить на 3 вопроса", font='Arial 20')
    text.pack()

def first_text_of_question():
    question = Label(master, text="-3 + 3", font='Arial 15', bg="red")
    question.pack()

def add_element_event(event=None):
    current = entry_field.get()
    entry_field.insert(0, str(current) + str(event))
    answers.append(current)

    print(answers)

def another_quest():
    second_text()
    second_text_of_question()

def second_text():
    text = Label(master, text="Вам осталось ответить на 2 вопроса", font='Arial 20')
    text.pack()

def second_text_of_question():
    question = Label(master, text="7 * 2", font='Arial 15', bg="red")
    question.pack()

def btn():
    btn = Button(master, text='Ответ', padx=15, pady=7, command=lambda: add_element_event())
    btn.pack()

first_text()
first_text_of_question()
entry_field = Entry(master,width=40,borderwidth=5)
entry_field.pack()
btn()    

master.mainloop()