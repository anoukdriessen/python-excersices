"""
results = data["results"]
for q in results:
    q_cat = q['category']
    q_type = q['type']
    q_difficulty = q['difficulty']
    question = q['question']
    correct = q['correct_answer']
    incorrect = q['incorrect_answers']
    all_answers = [correct]
    all_answers.extend(incorrect)

    print("********************************************************************")
    print(f"Category [{q_cat}] - {q_difficulty}")
    print(f"Type of question {q_type}")
    print(f"Q: {question}")
    print(f"{all_answers}")
    print("********************************************************************")
"""

class Question:

    def __init__(self, category, question, type, difficulty, correct_answer, answers):
        self.category = category                # category for the question
        self.question = question                # the question
        self.type = type                        # type of question (boolean / multiple)
        self.difficulty = difficulty            # the difficulty of the question [Easy/Medium/Hard]
        self.correct_answer = correct_answer    # the correct answer
        self.answer = answers                   # all possible answers