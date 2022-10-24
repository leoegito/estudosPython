from operator import truediv


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def checkAsnwer(self, given_answer):
        if given_answer == self.answer:
            return True
        else:
            return False