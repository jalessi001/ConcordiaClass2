

fName = input("Enter a file name: ")

try:
    f = open(fName, 'r')
    print(True)
except:
    print("File name is incorrect!")
