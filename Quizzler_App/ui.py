from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR,
                                 fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Question", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_img = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0,
                                   borderwidth=0, command=self.true)
        self.right_button.grid(row=2, column=0)

        wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0,
                                   borderwidth=0, command=self.false)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
