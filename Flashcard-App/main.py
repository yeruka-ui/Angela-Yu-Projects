import csv
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------------ RANDOM WORD --------------------------------- #
def next_card():
    '''Function is used to go to the next card when a button is clicked.'''
    global random_word, timer, word_list
    window.after_cancel(timer)
    random_word = random.choice(word_list)
    canvas.itemconfig(c_img, image=f_card)
    canvas.itemconfig(t_txt, text= "French", fill= "black")
    canvas.itemconfig(l_txt, text= random_word["French"], fill="black")
    timer = window.after(3000, flip_card)

# ------------------------------------ KNOWN CARD -------------------------------- #
def is_known():
    word_list.remove(random_word)
    pd.DataFrame(word_list).to_csv("data/words_to_learn.csv", index= False)
    next_card()

# ------------------------------------ UNKNOWN CARD -------------------------------- #
def is_unknown():
    next_card()

# ------------------------------------ FLIP CARD -------------------------------- #
def flip_card():
    global random_word
    canvas.itemconfig(c_img, image= b_card)
    canvas.itemconfig(t_txt, text="English", fill= "white")
    canvas.itemconfig(l_txt, text=random_word["English"], fill="white")

# ---------------------------------------------- START -------------------------------------------------------- #
'''This section is where the program starts. This uses try-except for checking for words to learn or if the user is a new user. 
Additionally, it makes use of the functions above when flipping cards or when the right or wrong buttons are clicked.'''
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
except pd.errors.EmptyDataError:
    df = pd.read_csv("data/french_words.csv")
finally:
    random_word = {}
    word_list = df.to_dict(orient="records")

    window = Tk()
    canvas = Canvas(width= 800, height= 526, highlightthickness= 0, bg= BACKGROUND_COLOR)
    window.title("Flashcard App")
    window.config(padx= 50, pady= 50, bg = BACKGROUND_COLOR)

    timer = window.after(3000, flip_card)

    # Card UI
    f_card =  PhotoImage(file="images/card_front.png")
    b_card = PhotoImage(file="images/card_back.png")
    c_img = canvas.create_image(400, 263, image = f_card)
    canvas.grid(column= 0, row= 0, columnspan= 2)

    t_txt = canvas.create_text(400, 150, text= "", fill= "black", font= ("Ariel", 40, "italic"))
    l_txt = canvas.create_text(400, 263, text= "", fill= "black", font= ("Ariel", 60, "bold"))

    # Buttons
    r_btn_img = PhotoImage(file= "images/right.png")
    r_btn = Button(image= r_btn_img, highlightthickness= 0, bd= 0, command= is_known)
    r_btn.grid(column= 1, row= 1)

    w_btn_img = PhotoImage(file= "images/wrong.png")
    w_btn = Button(image= w_btn_img, highlightthickness= 0, bd= 0, command= is_unknown)
    w_btn.grid(column= 0, row= 1)

    next_card()

window.mainloop()