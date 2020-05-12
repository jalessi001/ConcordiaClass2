myList = ['red', 'green', 'blue']

myList = myList + ["black", "white"]

myList[2] = 'yellow'

del myList[1]

myList.remove("red")

i = 1
for a in myList:
    print(str(i) + " " + a.capitalize())
    i += 1