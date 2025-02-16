# Please write a program which asks the user for a temperature in degrees Fahrenheit,
# and then prints out the same in degrees Celsius.
# If the converted temperature falls below zero degrees Celsius,
# the program should also print out "Brr! It's cold in here!".

F = int(input("Please type in a temperature (F):"))
C = ((F - 32) * 5 ) / 9

print(f"{F} degrees Fahrenheit equals {C} degrees Celsius")

if C < 0:
    print("Brr! It's cold in here!")