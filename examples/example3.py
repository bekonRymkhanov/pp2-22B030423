import csv
with open('sometable.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|',)
    for row in spamreader:
        print(row[0])