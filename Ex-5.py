groupSize = int(input("How many people are in your dinner group?: "))

if groupSize > 8:
    print("As group size is %d, you will have to wait for a table." % groupSize)
else:
    print("We have a table ready for you!")