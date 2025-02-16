input_str = input("What year were you born?")
year = int(input_str)

# you can directly convert the input in int
year_int = int(input("What year were you born?"))

# same with the other number datatypes
weight = float(input("How much do you weight?"))
height = float(input("What is your height?"))


# ask for name and year
name = input("What is your name?")
year_born = int(input("What year were you born?"))

age = 2021 - year_born

print(f"Hi {name}, you will be {age} years old at the end of the year 2021")

# print sum and mean
# Write your solution here
number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
number3 = int(input("Number 3:"))
number4 = int(input("Number 4:"))

sumOfNumbers = number1 + number2 + number3 + number4
mean = sumOfNumbers / 4

print(f"The sum of the numbers is {sumOfNumbers} and the mean is {mean}")