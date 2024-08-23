import random


def main():
    score=0
    digit=generate_integer(get_level())
    for _ in range(10):
        upper_bound=pow(10,digit)-1
        x=random.randint(1,upper_bound)
        y=random.randint(1,upper_bound)
        z=x+y
        for i in range(3):
            answer=int(input(f"{x}+{y}="))
            if answer==z:
                score+=1
                break
            elif i==2:
                print(f"{x}+{y}={z}")
            else:
                print("EEE")
    print(f"score is {score}")




def get_level():

    n=input("level:")
    return n


def generate_integer(level):
    while True:
        try:
            level=int(level)
            if  level>3 or level<1:
                raise ValueError
            else:
                return level
        except ValueError:
            level=get_level()
            continue
    

if __name__ == "__main__":
    main()