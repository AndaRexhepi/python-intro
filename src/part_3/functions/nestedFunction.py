# You can call a function from within another function.
# In fact, we have done so many times before, when we called
# the print function within our own functions in the previous part

def greet(name):
    print("Hello {n}".format(n = name))

def greet_many_times(times):
    while times >= 0:
        greet("Anda")
        times -= 1

greet_many_times(4)