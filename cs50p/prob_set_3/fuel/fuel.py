while True:
    try:
        x,y=map(int,input("Fraction:").strip().split("/"))
        if y==0:
            raise ZeroDivisionError
        z=x/y*100
        if z>100 or z<0:
            raise ValueError
        elif z>=99:
            print("F")
        elif z<=1:
            print("E")
        else:
            print(f"{z}%")
        break
    except ValueError:
        print("you should input correct X and Y")
    except ZeroDivisionError:
        print("y cannot be 0")
        
    
        