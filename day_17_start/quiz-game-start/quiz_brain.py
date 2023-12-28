class QuizBrain():
    def __init__(self, list):
        self.number = 0
        self.list = list
        self.score = 0

    def still_has_question(self):
        return self.number < len(self.list)

    def next_question(self):
        current_question = self.list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}: {current_question.text} \nTrue or False: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("That is correct")
            self.score += 1
        else:
            print("that is incorrect")
        print(f"the correct answer was {answer}")
        print(f"Your current score is {self.score} / {self.number} \n")