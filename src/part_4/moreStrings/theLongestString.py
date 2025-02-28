# Please write a function named longest(strings: list),
# which takes a list of strings as its argument.
# The function finds and returns the longest string in the list.
# You may assume there is always a single longest string in the list.


def longest(strings: list):
    list_of_lengths = [len(item) for item in strings]
    longest_string = max(list_of_lengths)
    longest_string_index = list_of_lengths.index(longest_string, 0, len(list_of_lengths))
    return strings[longest_string_index]

list_strings = ["Book", "Python", "Anda", "Notebook"]

print(longest(list_strings))




