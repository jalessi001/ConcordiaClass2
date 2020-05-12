twoPower = [pow(2, exponent) for exponent in range(0, 11)]
print(twoPower)

mylist = ["A", "B", "C"]
mylist2 = ['abc', mylist, [1, 2, 3]]
item1 = mylist2[2][2]
item2 = mylist2[0]
item3 = item2[2]                             # every string is a list of characters!!!
item4 = mylist2[1][1]

print(item1, item2, item3, item4)

