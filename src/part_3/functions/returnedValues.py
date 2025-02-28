# functions can return values which we can then use and print

def add(a,b):
    return a +b

result = add(3,5)
print(result)

# you can also define their data type which is not always necessary because
# it is not a guarantee of reduced type errors or a safeguard

def print_many_times(message :str, times: int):
    print(message * times)


print_many_times("Hello Anda", 4)
