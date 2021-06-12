from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")

        self.question_canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.question_canvas.create_text(
            150,
            125,
            text="Placeholder",
            font=("Arial", 20, "italic"),
            width=280
        )
        self.score_label = Label(bg=THEME_COLOR, fg="white", text=f"Score: {self.score}")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_clicked)
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_clicked)

        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score_label.grid(row=0, column=1)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.change_question()

        self.window.mainloop()

    def up_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

    def change_question(self):
        self.white_canvas()
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)


    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, correct: bool):
        if correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000)
        self.change_question()
        # self.white_canvas()

    def white_canvas(self):
        self.question_canvas.config(bg="white")
