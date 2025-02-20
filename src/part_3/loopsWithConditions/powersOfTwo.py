# Please write a program which asks the user to type in an upper limit.
# The program then prints out numbers so that each subsequent number is
# the previous one doubled, starting from the number 1.
# That is, the program prints out powers of two in order.

number = int(input("Upper limit:"))
counter = 1

while counter <= number:
    print(counter)
    counter *= 2