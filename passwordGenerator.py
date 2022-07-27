#Password Generator in python3, without the use of random methods - except randint)
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersUpperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['%', '(', ')', '@', '!', '#', '$', '&', '*',
           '-', '_', '=', '.', ',', ';', ':', '~']

choice = random.randint(0, 3)
print("Password Generator - Python3")
numberLetters = int(
    input("How many letters would you like in your password?\n"))
numberSymbols = int(
    input("How many symbols would you like in your password?\n"))
numberNumbers = int(input("How many numbers would you like?\n"))

passLetters = f""
passSymbols = f""
passNumbers = f""
i = 0
j = 0
k = 0
while i < numberLetters:
    if random.randint(0, 1) == 0:
        passLetters += letters[random.randint(0, 25)]
    else:
        passLetters += lettersUpperCase[random.randint(0, 25)]
    i += 1

while j < numberSymbols:
    passSymbols += symbols[random.randint(0, len(symbols)-1)]
    j += 1

while k < numberNumbers:
    passNumbers += numbers[random.randint(0, len(numbers)-1)]
    k += 1

password = passLetters+passSymbols+passNumbers
passwordAsAList = []

for character in password:
    passwordAsAList.append(character)

for i in range(0, len(passwordAsAList)):
    randomizer = random.randint(0, len(passwordAsAList)-1)
    temp = password[i]
    passwordAsAList[i] = passwordAsAList[randomizer]
    passwordAsAList[randomizer] = temp

password = ''.join(passwordAsAList)
print("Generated password:")
print(password)
