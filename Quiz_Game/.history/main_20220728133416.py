from question_model import Question
from data import question_data

question_bank=[]
for i in range(len(question_data)):
    q=question_data[i]['text']
    a=question_data[i]['answer']
    question=Question(q,a)
    question_bank.append(question)

print(question_bank[0].text)
print(question_bank[0].answer)
