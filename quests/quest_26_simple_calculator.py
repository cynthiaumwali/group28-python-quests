#!/usr/bin/python3

first_number = int(input("First number? - "))
second_number = int(input("Second number? - "))
operation = input(f"""What operation do you want? Choose accordingly:
{first_number} + {second_number} [+]
{first_number} - {second_number} [-]
{first_number} × {second_number} [*]
{first_number} ÷ {second_number} [/]
Your choice - """)

def add(numOne, numTwo):
    return numOne + numTwo

def subtract(numOne, numTwo):
    return numOne - numTwo

def divide(numOne, numTwo):
    return numOne / numTwo

def multiply(numOne, numTwo):
    return numOne * numTwo

if operation == "+":
    print(f"{first_number} + {second_number} = {add(first_number, second_number)}")
elif operation == "-":
    print(f"{first_number} - {second_number} = {subtract(first_number, second_number)}")
elif operation == "*":
    print(f"{first_number} × {second_number} = {multiply(first_number, second_number)}")
elif operation == "/":
    if second_number == 0:
        print(f"{first_number} ÷ {second_number} - Can't divide by zero")
    else:
        print(f"{first_number} + {second_number} = {divide(first_number, second_number)}")
else:
    print("Invalid operation chosen.")
