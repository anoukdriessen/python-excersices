from question import Question
from data import quiz_data
from quiz import GameLogic
from ui import Interface

# list to store all questions
questions = []
for q in quiz_data:
    answers = [q['correct_answer']]
    answers.extend(q['incorrect_answers'])
    # create question object
    new_question = Question(
        category=q['category'],
        question=q['question'],
        type=q['type'],
        difficulty=q['difficulty'],
        correct_answer=q['correct_answer'],
        answers=answers
    )
    # add to list
    questions.append(new_question)

quiz = GameLogic(questions) # create the game logic based on the questions
interface = Interface(quiz) # create the interface based on the logic