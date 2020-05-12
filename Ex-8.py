while True:
    multiple = input("Input quit to leave program. Please provide a number: ")
    if multiple == "quit":
        print("Goodbye.")
        break
    if int(multiple) % 10 == 0:
        multiple = int(multiple)
        print("%d is divisible by 10." % multiple)
    else:
        multiple = int(multiple)
        print("%d is not divisible by 10." % multiple)