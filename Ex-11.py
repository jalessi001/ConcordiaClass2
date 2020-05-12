import random

a = 1  # This should be the lower limit.
b = 100  # This should be the upper limit.

x = random.randint(a, b)

y = int(input("Please enter a number between %d and %d: " % (a, b)))

t = 1  # number of tries ; should start at one

while True:
    if x == y:
        print("You chose %d, which is the correct number! It took you %d attempts." % (y, t))
        break
    elif x != y:
        if x > y:
            print("The number you selected is lower than the answer. Try again.")
        elif x < y:
            print("The number you selected is higher than the answer. Try again.")
        t += 1
        y = int(input("Please enter a number between %d and %d: " % (a, b)))
