# Please write a program which asks the user for an integer number.
# If the number is divisible by three, the program should print out Fizz.
# If the number is divisible by five, the program should print out Buzz.
# If the number is divisible by both three and five, the program should print out FizzBuzz.

number = int(input("Number:"))

divByThree = number % 3 == 0
divByFive = number % 5 == 0


if divByThree and divByFive:
    print("FizzBuzz")
elif divByThree:
    print("Fizz")
elif divByFive:
    print("Buzz")