from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#fff7f2"
FONT_COLOR = "#cb5959"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.geometry("550x550")

        self.canvas = Canvas(width= 500, height= 330, highlightthickness= 0, bg= THEME_COLOR)
        self.canvas.grid(column=0, row=0)

        self.label = Label(text ="Quizler", font = ("Bauhaus 93", 30, 'bold'), fg = FONT_COLOR, bg = THEME_COLOR)
        self.label.grid(column = 0, row = 0, columnspan= 2)

        #quiz_img
        self.photo_img = PhotoImage(file= "images/Quizzler.png")
        self.canvas.create_image(30, 10, image=self.photo_img, anchor="nw")
        self.canvas.grid(column=0, row=1, columnspan= 2)

        #false/true btn
        self.true_btn_img = PhotoImage(file="images/true.png")
        self.t_btn = Button(image=self.true_btn_img, highlightthickness=0, bd=0, bg= THEME_COLOR, command= self.true_pressed)
        self.t_btn.grid(column=0, row=2)

        self.false_btn_img = PhotoImage(file="images/false.png")
        self.f_btn = Button(image=self.false_btn_img, highlightthickness=0, bd=0, bg= THEME_COLOR, command= self.false_pressed)
        self.f_btn.grid(column=1, row=2)

        #score
        self.score = self.canvas.create_text(self.canvas.winfo_reqwidth() // 2, 80,
                                             text= f"Score -  ",
                                             fill= FONT_COLOR,
                                             font= ("Bauhaus 93", 16))

        #question
        self.question = self.canvas.create_text(self.canvas.winfo_reqwidth() // 2, 170,
                                             text=f"",
                                             width= 280,
                                             fill=FONT_COLOR,
                                             font=("Arial Rounded MT", 16, 'bold'))

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=THEME_COLOR)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text= q_text)
        else:
            self.canvas.itemconfig(self.question, text= "Complete!\nWell done!")
            self.t_btn.config(state="disabled")
            self.f_btn.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg= "#d9ffd7")
            self.quiz.score += 1

        else:
            self.canvas.config(bg= "#ffd7d7")

        self.window.after(1000, self.get_next_question)
        self.canvas.itemconfig(self.score, text=f"Score - {self.quiz.score}")
