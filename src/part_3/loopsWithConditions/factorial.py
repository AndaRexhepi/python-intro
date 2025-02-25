# Please write a program which asks the user to type in an integer number.
# If the user types in a number equal to or below 0, the execution ends.
# Otherwise, the program prints out the factorial of the number.

i = 1
result = 1
while True:
     number = int(input("Please type in a number: "))

     if number <= 0:
         print("Thanks and bye!")
         break
     else:
         while i <= number:
             result *= i
             i += 1
     print(f"The factorial of the number {number} is {result}")
     result = 1
     i = 1