from tkinter import *
from quiz import GameLogic

THEME_COLOR = "#375362"

class Interface:
    def __init__(self, quiz: GameLogic):
        # import the logic
        self.quiz = quiz

        # create the ui
        self.window = Tk()
        self.window.title("My amazing quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # keep track of the score
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # create a canvas for the question
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
   
        # button for True
        true_image = PhotoImage(file="./source/practice_projects/trivia_game/img/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.clicked_true)
        self.true_button.grid(row=2, column=0)

        # button for False
        false_image = PhotoImage(file="./source/practice_projects/trivia_game/img/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.clicked_false)
        self.false_button.grid(row=2, column=1)        

        # method to load next question
        self.get_next_question()

        self.window.mainloop()

    # method to get next question
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # if the user clicks true
    def clicked_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    # if the user clicks false
    def clicked_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    # method to give feedback to the answer of the user
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)    