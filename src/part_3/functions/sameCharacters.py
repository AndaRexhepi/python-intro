# Please write a function named same_chars, which takes one string
# and two integers as arguments. The integers refer to indexes within
# the string. The function should return True if the two characters
# at the indexes specified are the same. Otherwise, and especially
# if either of the indexes falls outside the scope of the string,
# the function returns False.

def same_chars(word, first_number, second_number):
    length = len(word)
    if ((first_number < 0 or first_number > length) or
            (second_number < 0 or second_number > length)):
        return False
    elif word[first_number].lower() == word[second_number].lower():
        return True
    else:
        return False


value = same_chars("Anda", 0, 5)
print(value)
