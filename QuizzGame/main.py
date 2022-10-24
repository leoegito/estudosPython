from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

# Loop through questions dictionary, create question object for each one,
# then add to a list
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")
