import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match:=re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(\w+)"',s):
        id=match.group(1)
        return f"https://youtu.be/{id}"
    return None



if __name__ == "__main__":
    main()