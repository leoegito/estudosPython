# Guess the number game, 1 to 100, two diferent levels: easy and hard
import random
from tkinter.tix import INTEGER
# Hard level: 5 guesses
HARD_LEVEL = 5
# Easy level: 10 guesses
EASY_LEVEL = 10


def generateNumber():
    return random.randint(1, 100)


def guess(asnwer, secret):
    if asnwer < secret:
        print("Too low. Try again.")
        return False
    elif asnwer > secret:
        print("Too high. Try again.")
        return False
    else:
        print(f"Tah-dah! Gratz, you guessed it right! The number is {secret}")
        return True


def game():
    chances = 0
    secret = generateNumber()
    level = input("Choose the dificulty: 'easy' or 'hard'\n")
    if level == 'easy':
        chances = EASY_LEVEL
    else:
        chances = HARD_LEVEL
    while chances > 0:
        asnwer = int(input("Type the number (integer, 1~100): "))
        if not guess(int(asnwer), secret):
            chances -= 1
        else:
            return
    if chances == 0:
        print("You lose.")


while True:
    play = input("Do you wanna play 'guess the number'? 'y' or 'n'\n")
    if play == 'y':
        game()
    else:
        break
