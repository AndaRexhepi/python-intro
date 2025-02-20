# Please write a program which asks the user for a string.
# The program then prints out a message based on whether
# the second character and the second to last character are the same or not.

string = input("Please type in a string: ")
second = string[1]
secondToLast = string[-2]


if second == secondToLast:
    print(f"The second and the second to last characters are {second}")
else:
    print("The second and the second to last characters are different")