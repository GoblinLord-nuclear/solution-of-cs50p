def main():
    fraction=input("INPUT:").strip()
    z=convert(fraction)
    string=gauge(z)
    print(string)

def convert(fraction):
    while True:
        try:
            x,y=map(int,fraction.split("/"))
            if y==0:
                raise ZeroDivisionError
            z=x/y*100
            if z>100 or z<0:
                raise ValueError
            return round(z)
        except ValueError:
            print("you should input correct X and Y")
            fraction=input("INPUT:").strip()
            continue
        except ZeroDivisionError:
            print("y cannot be 0")
            fraction=input("INPUT:").strip()
            continue
        


def gauge(percentage):
    if percentage>=99:
        return "F"
    elif percentage<=1:
        return "E"
    else:
        return (f"{percentage}%")



if __name__ == "__main__":
    main()