import html

class GameLogic:
    def __init__(self, list_of_questions):
        self.question_number = 0
        self.score = 0
        self.list_of_questions = list_of_questions
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.list_of_questions)

    def next_question(self):
        self.current_question = self.list_of_questions[self.question_number]
        self.question_number += 1
        question = html.unescape(self.current_question.question)
        return f"Q.{self.question_number}: {question}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            # print("You got it right!")
            return True
        else:
            # print("That's wrong.")
            return False