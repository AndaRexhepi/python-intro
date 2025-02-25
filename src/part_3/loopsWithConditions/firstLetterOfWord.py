# Please write a program which asks the user to type in a sentence.
# The program then prints out the first letter of each word in the sentence,
# each letter on a separate line.

string = input("Please type in a sentence: ")

length = len(string)

i = 0

while i <= length -1:
    if i == 0 and string[i] != " ":
        print(string[i])
        i += 1
    elif i > 0 and string[i] == " ":
        print(string[i + 1])
        i += 1
    else:
        i += 1