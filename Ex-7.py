value = int(input("Please provide a value between 0 and 100: "))
v2 = value % 2
v5 = value % 5

if (value > 100) or (value < 0):
    print("You provided an incorrect value.")
elif (v2 == 0) and (v5 == 0):
    print("highFive and HighEven")
elif v2 == 0:
    print("HiEven")
elif v5 == 0:
    print("HiFive")
else:
    print("Good job!")








