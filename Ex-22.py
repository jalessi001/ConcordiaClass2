import csv

f = open("100 Sales Records.csv", 'rt')  # to read as a text file

reader = csv.reader(f)
next(f)

counter = 0
unitsSoldEurope = 0
unitsSoldTotal = 0
itemTypes = {}

for row in reader:
    unitsSoldTotal = unitsSoldTotal + int(row[8])
    itemTypes[row[2]] = row[3]

    if row[0] == "Europe":
        counter += 1
        unitsSoldEurope = int(row[8]) + unitsSoldEurope

print("Order records from Europe is: %d" % counter)
print("Units sold in Europe is: %d" % unitsSoldEurope)
print("Units sold worldwide is: %d" % unitsSoldTotal)

list = itemTypes.keys()
print(list)