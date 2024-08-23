import tabulate
import sys
import csv
try:
    if len(sys.argv)>2:
        raise IndexError
    file=sys.argv[1]
    if not file.endswith(".csv"):
        raise NameError
    with open(file) as csvfile:
        csv_file=csv.DictReader(csvfile)
        output_file=tabulate.tabulate(csv_file,headers="keys",tablefmt="grid")


        print(output_file)
except IndexError:
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    sys.exit("Too few command-line arguments")
except NameError:
    sys.exit("Not a CSV file")
except FileNotFoundError:
    sys.exit("File does not exist")