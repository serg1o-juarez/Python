from art import logo
import os

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    '+': add,
    '-':subtract,
    '*':multiply,
    '/':divide,
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number.\n"))
    for operation in operations:
        print(operation)
    operation_symbol = input("Pick an operation from the line above. ")
    num2 = float(input("What is the second number.\n"))

    keep_calculating = True
    while keep_calculating:
        calculate = operations[operation_symbol]
        answer = calculate(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        cont= input(f"type 'y' to continue calculating with {answer},type 'n' to quit, or type 'c' to start a new calculation: ").lower()
        if cont == 'y':
            num1 = answer
            operation_symbol = input("Pick an operation: ")

            num2 = int(input("What is the next number.\n"))
        elif cont == 'c':
            keep_calculating = False
            os.system('clear')
            calculator()
        elif cont == 'n':
            keep_calculating = False

calculator()
