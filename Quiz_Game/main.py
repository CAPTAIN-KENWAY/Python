from question_model import Question
from data import question_data, logo
from quiz_brain import QuizBrain
from os import system

question_bank = []
for i in question_data:
    q = i['question']
    a = i['correct_answer']
    question = Question(q, a)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
system("CLS")
print(logo)
while quiz.still_has_questions() == True:
    quiz.next_question()
    quiz.check_answer()
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
