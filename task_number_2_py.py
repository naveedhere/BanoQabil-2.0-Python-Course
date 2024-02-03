# -*- coding: utf-8 -*-
"""Task_Number_2.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CaNoIEd98KRky2dEGUudrcKvsKvytoud
"""

#NAME: NAVEED
#EMAIL: mn815325@gmail.com

#CALCULATOR IN PYTHON

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")
    print("------------------")

    while True:
        # Take operator input
        operator = input("Enter operator (+, -, *, /) or 'exit' to end: ").lower()

        if operator == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        # Take numeric inputs
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform calculation based on the operator
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator. Please enter +, -, *, or /.")
            continue

        # Display the result
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()

