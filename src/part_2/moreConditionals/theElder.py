# Please write a program which asks for the names and ages of two persons.
# The program should then print out the name of the elder.

print("Person 1:")
p1Name = input("Name:")
p1Age = int(input("Age:"))

print("Person 2:")
p2Name = input("Name:")
p2Age = int(input("Age:"))

if p1Age > p2Age:
    print(f"The elder is {p1Name}")
elif p1Age < p2Age:
    print(f"The elder is {p2Name}")
else:
    print(f"{p1Name} and {p2Name} are the same age")