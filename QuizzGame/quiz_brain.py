from contextlib import nullcontext


class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
    
    # def next_question(self):
    #     self.question_number += 1

    # def round_question(self):
    #     return self.questions_list[self.question_number]

    def check_answer(self, user_answer, current_question_answer):
        if user_answer.lower() == current_question_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong answer.")
        print(f'The correct answer is: {current_question_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}\n')

    def still_has_questions(self):
        if self.question_number >= len(self.questions_list):
            return False
        return True
        # it could be return self.question_number < len(self.questions_list)

    def next_question(self):
        current = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current.text} (True/False)?: ')
        self.check_answer(user_answer, current.answer)
