from tkinter import *
from tkinter.ttk import Combobox
import random
from random import randrange


f_name = input('Enter Your First Name: ')
l_name = input('Enter Your Last Name: ')
dob = input('Enter Birth Year:')


screen = Tk()
screen.title("Username Generator")
screen.geometry("600x400")
screen.configure(background="Cyan")


def generate():
    global username
    username.set("")
    number = [dob, dob[-2:], dob[:2], randrange(9999)]
    first = [f_name, f_name[:1]]
    gen = (str(random.choice(first)) +
           l_name + str(random.choice(number)))
    username.set(gen)


# Tkinter

username = StringVar('')

t1 = Label(screen, text='Username Generator',
           font=('Arial', 25), fg='red', background="bisque")
t1.place(x=60, y=0)

t2 = Label(screen, text='Username:', font=('Arial', 14), background="bisque")
t2.place(x=145, y=90)

il = Entry(screen, font=('Arial', 14), textvariable=username)
il.place(x=270, y=90)

b = Button(screen, text='Generate', font=(
    'Arial', 14), fg='red', background="white", command=generate)
b.place(x=230, y=195)


screen.mainloop()
