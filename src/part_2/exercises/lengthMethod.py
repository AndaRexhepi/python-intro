# The len method is used to return the length of a string literal
word = input("Please type in a word: ")

length = len(word)

if length > 1:
    print(f"There are {length} letters in the word {word}")

print("Thank you!")