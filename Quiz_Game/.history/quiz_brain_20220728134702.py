class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list

    def next_question(self):
        input(f"Q.{self.question_number+1}: {self.questions_list[self.question_number].text} (True/False): ")
        self.question_number += 1

    def still_has_questions(self):
        pass