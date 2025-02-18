# Python comparison operators can also be used on strings.
# String a is smaller than string b if it comes alphabetically before b.

# Please write a program which asks the user for two words.
# The program should then print out whichever of the two comes alphabetically last.

first_word = input("Please type in the 1st word:")
second_word = input("Please type in the 2nd word:")

if first_word > second_word:
    print(f"{first_word} comes alphabetically last.")
elif first_word < second_word:
    print(f"{second_word} comes alphabetically last.")
else:
    print("You gave the same word twice.")