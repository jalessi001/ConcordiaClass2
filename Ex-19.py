import os

while True:

    fName = input("Enter a file name: ")

    if os.path.exists(fName):
        print(True)
        break
    else:
        print("File name is incorrect!")


