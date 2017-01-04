import csv
with open("csvFiles/test.csv") as f:
    myData = csv.reader(f, delimiter=' ', quotechar='|')
    for row in myData:
        print(', '.join(row))



