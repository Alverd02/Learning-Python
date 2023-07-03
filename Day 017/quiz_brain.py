class QuizBrain:
    def __init__(self, question_list):
        self.guess = None
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        if self.question_number <= 11:
            self.guess = input(
                f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ").lower()


    def still_has_questions(self):
        q_number = len(self.question_list)
        return self.question_number < q_number

    def check_answer(self):
        if self.guess == self.question_list[self.question_number].answer.lower():
            self.score += 1
            print(f"Score = {self.score}/{self.question_number+1}")
        else:
            print(f"Score = {self.score}/{self.question_number+1}")
        self.question_number += 1
