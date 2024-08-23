import sys
import csv
try:
    if len(sys.argv)>2:
        raise IndexError
    file=sys.argv[1]
    if not file.endswith(".csv"):
        raise NameError
    with open(file) as csvfile:
        input_file=csv.DictReader(csvfile)
        with open("after.csv","w",newline="")as after_csv:
            fieldnames_=["firstname","lastname","house"]
            writer=csv.DictWriter(after_csv,fieldnames=fieldnames_)
            writer.writeheader()
            for i in input_file:
                first,last=i["name"].split(", ")
                writer.writerow({"firstname":first,"lastname":last,"house":i["house"]})
except IndexError:
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    sys.exit("Too few command-line arguments")
except NameError:
    sys.exit("Not a CSV file")
except FileNotFoundError:
    sys.exit("File does not exist")