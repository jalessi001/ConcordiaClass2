while True:
    num = input("Please provide a number: ")

    if int(num) % 2 == 0:
        print("%d is an even number!" % int(num))
    elif int(num) % 2 != 0:
        print("%d is not an even number!" % int(num))

    prompt = input("Do you wish to continue? (yes or no): ")

    if prompt == "no":
        print("Goodbye!")
        break