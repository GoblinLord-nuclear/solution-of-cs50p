from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
if len(sys.argv)==1:
    f=random.choice(figlet.getFonts())
elif len(sys.argv)==3:
    if sys.argv[1]=="-f"or sys.argv[1]=="--font":
        f=sys.argv[2]
        if f not in figlet.getFonts():
            print("invalid usage")
            sys.exit()
    else:
        print("invalid usage")
        sys.exit()
else:
    print("invalid usage")
    sys.exit()
figlet.setFont(font=f)
text=input("Input: ")
print(figlet.renderText(text))
