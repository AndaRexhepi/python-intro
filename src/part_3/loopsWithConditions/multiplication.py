# Please write a program which asks the user for a positive integer number.
# The program then prints out a list of multiplication operations until
# both operands reach the number given by the user

number = int(input("Please type in a number: "))

i = 1

while number >= i:
    operand = 1
    while operand <= number:
        print(f"{i} x {operand} = {i * operand}")
        operand += 1
        if operand > number:
            i += 1
            break