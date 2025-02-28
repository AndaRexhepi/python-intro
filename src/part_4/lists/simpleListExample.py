# you can define lists like this:

my_first_list = [] # which is empty

another_list = [1,2,3,4,5]

# we can access list items like this
item = another_list[3]
print(item)

# you can print out the whole content of the list
print(another_list)

#lists are mutable which means you can change their values and/or items
another_list[3] = 10
print(another_list)

#this way we can return the length of the list
length = len(another_list)
print(length)

# this is how you can add items to a list
another_list.append(6)
print(another_list)

# if you want to add an item to a specific location
another_list.insert(0,4)
another_list.insert(4,10)
print(another_list)

#if you want to remove an item from the list you can do it in two ways
# use pop() when you want to remove by index
# and use remove() when you want to remove by value

another_list.pop(0) # this will remove the first element and returns it
another_list.pop(3) # this will remove the number 3 from the list
print(another_list)

#we can sort a list by .sort() method and sorted()
another_list.sort() # sorts the list itself
sorted_ls = sorted(another_list) # whereas here we create a copy of the sorted list without
# modifying the existing one
print(another_list)
print(sorted_ls)

# you can find the minimum, maximum or the sum of all the elements of the list
greatest = max(another_list)
smallest = min(another_list)
sum_list = sum(another_list)

print(greatest)
print(smallest)
print(sum_list)






