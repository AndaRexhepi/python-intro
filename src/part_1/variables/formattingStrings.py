
# this is how you print mixed type variables in string easily by formatting
result = 10 * 20
print(f"Result is {result}")

name = "Anda"
age = 19
print(f"My name is {name} and I am {age} years old!")


name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old")
print()
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})")
print()
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")



x = 27
y = 15

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

# print a single line by using end=""
print("Hello ", end="")
print("Anda")


number = int(input("Please type in a number: "))

print(f"{number} times 5 is {number * 5}")