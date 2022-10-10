# Calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

n1 = int(input("What is the first number? "))
n2 = int(input("What is the second number? "))

for operation in operations:
    print(operation)

operationSymbol = input("Pick the operation from the list above: ")

if operationSymbol in operations:
    answer = operations[operationSymbol](n1, n2)
else:
    answer = "Pick one of the operations available."


print(f'{n1} {operationSymbol} {n2} = {answer}')
