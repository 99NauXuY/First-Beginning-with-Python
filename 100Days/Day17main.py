from Day17question_model import Question
from Day17data import question_data
from Day17quiz_brain import QuizBrain

question_bank = []
for elements in question_data:
    question_bank.append(Question(elements['text'], elements['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")