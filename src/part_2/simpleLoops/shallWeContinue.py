# Let's create a program along the lines of the example above.
# This program should print out the message
# "hi" and then ask "Shall we continue?" until the user inputs "no"

while True:
    answer = input("Shall we continue?")

    print("hi")

    if answer == "no":
        print("okay then")
        break
