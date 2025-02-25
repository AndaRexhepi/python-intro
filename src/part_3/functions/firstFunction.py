# Define functions using the def keyword and ()

def greet():
    print("Hello World")

# Execute the function by calling it
greet()

# Functions can also take arguments which are defined and passed into the ()

def greet_person(name):
    print("Hello {name}".format(name = name))

def add(a, b):
    print(a + b)

greet_person("Anda")
add(1,4)

