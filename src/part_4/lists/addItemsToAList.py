# Please write a program which first asks the user for the number
# of items to be added. Then the program should ask for the given
# number of values, one by one, and add them to a list in the order they were typed in.

number_of_items = int(input("How many items?"))
n = 0
my_list = []
while number_of_items > 0:

    n += 1

    item = int(input(f"Item {n}: "))

    my_list.append(item)


    number_of_items -= 1

print(my_list)