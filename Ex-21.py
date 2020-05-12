import csv

csv_data = [["StudentId", "Grade"], [123456, "A"], [245678, "A"]]

with open('person.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csv_data)