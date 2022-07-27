import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# rules: no function, no class, etc
# code
playerChoice = int(input("Press 0 for rock, 1 for paper or 2 for scissors."))
if playerChoice < 0 or playerChoice > 2:
    print("Invalid option.")
    exit
# random.seed()
enemyChoice = random.randint(0, 2)
if enemyChoice == 0:
    if playerChoice == 0:
        print(rock+rock)
        print("Draw!")
    elif playerChoice == 1:
        print(paper+rock)
        print("You win.")
    else:
        print(scissors+rock)
        print("You lose.")
elif enemyChoice == 1:
    if playerChoice == 0:
        print(rock+paper)
        print("You lose.")
    elif playerChoice == 1:
        print(paper+paper)
        print("Draw!")
    else:
        print(scissors+paper)
        print("You win.")
else:
    if playerChoice == 0:
        print(rock+scissors)
        print("You win.")
    elif playerChoice == 1:
        print(paper+scissors)
        print("You lose.")
    else:
        print(scissors+scissors)
        print("Draw!")
