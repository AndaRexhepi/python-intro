# Please write a program which asks the user for two strings and then
# prints out whichever is the longer of the two - that is,
# whichever has the more characters. If the strings are of equal length,
# the program should print out "The strings are equally long".


string1 = input("Please type in string 1: ")
string2 = input("Please type in string 2: ")

if len(string1) > len(string2):
    print(string1 + " is longer")
elif len(string2) > len(string1):
    print(string2 + " is longer")
else:
    print("The strings are equally long")