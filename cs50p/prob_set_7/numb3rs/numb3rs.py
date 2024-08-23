import re
import sys
             

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches:=re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$",ip):
        for part in matches.groups():
            print(part)
            if not 0<=int(part)<=255:
                return False
        return True
    return False
        



if __name__ == "__main__":
    main()