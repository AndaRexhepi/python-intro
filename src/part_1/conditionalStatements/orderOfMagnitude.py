# Please write a program which asks the user for an integer number.
# The program should then print out the magnitude of the number

number = int(input("Please type in a number:"))

if number < 1000:
    print("Number is smaller than 1000")

if number < 100:
    print("Number is smaller than 100")

if number < 10:
    print("Number is smaller than 10")

print("Thank you!")