from question_model import Question
from data import question_data

question_bank=[]
for i in range(question_data):
    q=i['text']
    a=i['answer']
    question=Question(q,a)
    question_bank.append(question)


