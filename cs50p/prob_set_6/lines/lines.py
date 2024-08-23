import sys
length=0
try:
    file=sys.argv[1]
    if len(sys.argv)>2:
        raise IndexError
    if not file.endswith(".py"):
        raise ValueError
    with open(file,"r") as r_file:
        for line in r_file:
            line=line.lstrip()
            if not line.startswith("#") and len(line):
                length+=1
    print(length)
except ValueError:
    sys.exit("Not a Python file")
except IndexError:
    if len(sys.argv)>2:
        sys.exit("Too many command--line argument")
    else:
        sys.exit("Too few command--line argument")
except FileNotFoundError:
    sys.exit("File does not exist")