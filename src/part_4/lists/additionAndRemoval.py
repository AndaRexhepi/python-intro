# Please write a program which asks the user to choose between addition and removal.
# Depending on the choice, the program adds an item to or removes an item from the
# end of a list. The item that is added must always be one greater than the last
# item in the list. The first item to be added must be 1.

my_list = []
i = 0
while True:
    print("The list is now ", my_list)
    char = input("a(d)d, (r)emove or e(x)it: ")

    if char == "x":
        print("Bye!")
        break
    elif char == 'd':
        i += 1
        my_list.append(i)
    elif char == 'r':
        last_element = my_list[len(my_list) - 1]
        my_list.remove(last_element)