student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

for student in student_scores:
    score = "Fail"
    if student_scores[student] > 70:
        # student did not fail
        score = "Acceptable"
        if student_scores[student] > 80:
            score = "Exceeds Expectations"
            if student_scores[student] > 90:
                score = "Outstanding"

    student_grades[student] = score
    
print(student_grades)