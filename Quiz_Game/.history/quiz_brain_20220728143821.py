class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        self.answer = input(
            f"Q.{self.question_number+1}: {self.questions_list[self.question_number].text} (True/False): ").lower()
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self):
        ans=self.questions_list[self.question_number-1].answer
        if ans.lower()==self.answer:
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong.")
        print(f"The correct answer was {ans}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n\n")
    
