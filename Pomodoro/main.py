from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#3F7D58"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(tomato_time, text = "00:00")
    title_label.config(text =  "Timer")
    check_label.config(text = "")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS

    REPS += 1

    work_secs = 25 * 60
    short_break_secs = 5 * 60
    long_break_secs = 20 * 60

    if REPS % 8 == 0:
        title_label.config(text = "Long Break", fg = RED)
        count_down(long_break_secs)
    elif REPS % 2 == 0:
        title_label.config(text="Short Break", fg = PINK)
        count_down(short_break_secs)
    else:
        title_label.config(text="Work Time", fg = GREEN)
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(tomato_time, text = f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if REPS % 2 == 0:
            check = ""
            check += "✔️" * (REPS // 2)
            check_label.config(text = check)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodorie")
window.config(padx= 100, pady= 50, bg = YELLOW)

canvas = Canvas(width= 200, height= 224, bg = YELLOW, highlightthickness= 0)

# Tomato Label
title_label  = Label(text ="Timer", font = (FONT_NAME, 25, 'bold'), fg = GREEN, bg = YELLOW)
title_label.grid(column = 1, row = 0)

# Check Label
check_label = Label(font = (FONT_NAME, 10, 'bold'), fg = GREEN, bg = YELLOW)
check_label.grid(column = 1, row = 3)

# Tomato Buttons
# Start Button:
button_start = Button(text = "Start", highlightthickness = 0, command = start_timer)
button_start.grid(column = 0, row = 2)

# Reset Button:
button_reset = Button(text = "Reset", highlightthickness = 0, command = reset_timer)
button_reset.grid(column = 2, row = 2)

# Tomato Image
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
canvas.grid(column = 1, row = 1)
tomato_time = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 25, 'bold'))


window.mainloop()