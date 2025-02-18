# Please write a program which asks the user for three letters.
# The program should then print out whichever of the three letters
# would be in the middle if the letters were in alphabetical order.

firstLetter = input("1st letter:")
secondLetter = input("2nd letter:")
thirdLetter = input("3rd letter:")

if (secondLetter < firstLetter < thirdLetter) or (
        secondLetter > firstLetter > thirdLetter):
    print(f"The letter in the middle is {firstLetter}")
elif (firstLetter < secondLetter < thirdLetter) or (
        firstLetter > secondLetter > thirdLetter):
    print(f"The letter in the middle is {secondLetter}")
else:
    print(f"The letter in the middle is {thirdLetter}")
