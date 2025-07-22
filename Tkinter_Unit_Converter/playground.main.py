# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#     print(type(a))
#     print(type(args))
#     print(type(kw))

from tkinter import *

def click_button():
    entered_txt = u_input.get()
    my_label.config(text = entered_txt)

window = Tk()

window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=30, pady=30)

#Label
my_label = Label(text = "I am a Label", font = ("Arial", 24))
my_label.grid(column = 1, row = 1)

# Entry
u_input = Entry(width= 10)
u_input.grid(column = 4, row = 3)

# Button
button = Button(text = "Click", command = click_button)
button.grid(column = 2, row = 2)

# Button #2
button_2 = Button(text = "Click", command = click_button)
button_2.grid(column = 3, row = 1)

window.mainloop()