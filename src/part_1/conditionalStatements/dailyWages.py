# Please write a program which asks for the hourly wage, hours worked,
# and the day of the week. The program should then print out the daily wages,
# which equal hourly wage multiplied by hours worked,
# except on Sundays when the hourly wage is doubled.
from calendar import SUNDAY

hourlyWage = float(input("Hourly wage: "))
hoursWorked = int(input("Hours worked: "))
dayOfWeek = input("Day of the week: ")

if dayOfWeek == "Sunday":
    dailyWages = hourlyWage * 2 * hoursWorked
else:
    dailyWages = hourlyWage * hoursWorked

print(f"Daily wages: {dailyWages} euros")


print("What is the weather forecast for tomorrow?")

temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no):")

