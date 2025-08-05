from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"



# ------------------------------------ UI SETUP --------------------------------- #
window = Tk()
canvas = Canvas(width= 800, height= 526, highlightthickness= 0, bg= BACKGROUND_COLOR)
window.title("Flashcard App")
window.config(padx= 50, pady= 50, bg = BACKGROUND_COLOR)


# Card UI
f_card_img =  PhotoImage(file= "images/card_front.png")
canvas.create_image(400, 263, image = f_card_img)
canvas.grid(column= 0, row= 0, columnspan= 2)

canvas.create_text(400, 150, text= "Title", fill= "black", font= ("Ariel", 40, "italic"))
canvas.create_text(400, 263, text= "Word", fill= "black", font= ("Ariel", 60, "bold"))

# Buttons
r_btn_img = PhotoImage(file= "images/right.png")
r_btn = Button(image= r_btn_img, highlightthickness= 0, bd= 0)
r_btn.grid(column= 1, row= 1)

w_btn_img = PhotoImage(file= "images/wrong.png")
w_btn = Button(image= w_btn_img, highlightthickness= 0, bd= 0)
w_btn.grid(column= 0, row= 1)


window.mainloop()