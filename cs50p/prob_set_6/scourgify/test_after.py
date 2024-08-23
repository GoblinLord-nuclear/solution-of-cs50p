import csv
with open("after.csv") as csvfile:
        csvf=csv.DictReader(csvfile)
        for line in csvf:
            print(line)