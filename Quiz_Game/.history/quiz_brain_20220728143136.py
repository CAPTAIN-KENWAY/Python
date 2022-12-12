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
        return self.questions_list[self.question_number-1].answer.lower()==self.answer
