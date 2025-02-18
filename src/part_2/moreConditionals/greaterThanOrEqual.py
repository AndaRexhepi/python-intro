# Please write a program which asks for two integer numbers.
# The program should then print out whichever is greater.
# If the numbers are equal, the program should print a different message.

firstNumber = int(input("Please type in the first number:"))
secondNumber = int(input("Please type in another number: "))

if firstNumber > secondNumber:
    print(f"The greater number was {firstNumber}")
elif secondNumber > firstNumber:
    print(f"The greater number was {secondNumber}")
else:
    print("The numbers are equal!")
