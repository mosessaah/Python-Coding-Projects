class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        input(f"Q.{self.question_number+1}: {self.question_list[self.question_number]}. (True/False): ")
        self.question_number += 1

