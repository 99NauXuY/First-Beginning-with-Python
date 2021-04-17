class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = question_list

    def next_question(self):
        current = self.questions_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {current.text}. (True/False)?:")
        self.check_answer(choice, current.answer)

    def still_has_question(self):
        if self.question_number == len(self.questions_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")
