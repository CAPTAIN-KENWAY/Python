from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
    q=i['text']
    a=i['answer']
    question=Question(q,a)
    question_bank.append(question)

quiz=QuizBrain(question_bank)
quiz.next_question()
