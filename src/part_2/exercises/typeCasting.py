# Please write a program which asks the user for a floating point number
# and then prints out the integer part and the decimal part separately.
# Use the Python int function.

# You can assume the number given by the user is always greater than zero.

floating_number = float(input("Please type in a number: "))
rounded_number = int(floating_number)
decimal_part = floating_number - rounded_number

print(f"Integer part: {rounded_number}")
print(f"Decimal part: {decimal_part}")
