# Please write a program which asks the user for two numbers and an operation.
# If the operation is: add, multiply or subtract, the program should calculate and print
# out the result of the operation with the given numbers.
# If the user types in anything else, the program should print out nothing.

number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
operator = input("Operation: ")

if operator == "add":
    print(f"{number1} + {number2} = {number1 + number2}")

if operator == "multiply":
    print(f"{number1} * {number2} = {number1 * number2}")

if operator == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}")