import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersUpperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['%', '(', ')', '@', '!', '#', '$', '&', '*',
           '-', '_', '=', '.', ',', ';', ':', '~']

allowedCharacters = []
passwordList = []

print("Password Generator - Python3")

totallyRandom = int(
    input("Would you like a totally random password? 1 for YES, 0 for NO:\n"))

if totallyRandom == 1:
    numberOfCharacters = int(
        input("How many characters would you like in your password?\n"))
    allowedCharacters.extend(letters)
    allowedCharacters.extend(lettersUpperCase)
    allowedCharacters.extend(symbols)
    allowedCharacters.extend(numbers)
    random.shuffle(allowedCharacters)
    password = ''.join(random.choices(allowedCharacters, k=numberOfCharacters))

elif totallyRandom == 0:
    numberLetters = int(
        input("How many letters would you like in your password?\n"))
    numberSymbols = int(
        input("How many symbols would you like in your password?\n"))
    numberNumbers = int(input("How many numbers would you like?\n"))

    if numberLetters > 0:
        passwordLetters = []
        passwordLetters.extend(letters)
        passwordLetters.extend(lettersUpperCase)
        passwordList = random.choices(passwordLetters, k=numberLetters)

    if numberSymbols > 0:
        passwordList.extend(random.choices(numbers, k=numberNumbers))

    if numberNumbers > 0:
        passwordList.extend(random.choices(symbols, k=numberSymbols))

    random.shuffle(passwordList)
    password = ''.join(passwordList)

else:
    print("Invalid option. Aborting...")
    exit()

print(password)
