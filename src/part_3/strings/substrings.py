# Please write a program which asks the user to type in a string.
# The program then prints out all the substrings which begin with the
# first character, from the shortest to the longest.

word = input("Please type in a string:")

length = len(word)
counter = 0

while True:
    counter += 1

    print(word[0:counter])

    if counter == length:
        break