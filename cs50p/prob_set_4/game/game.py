import random
while True:
    try:
        n=int(input("level:"))
    except ValueError:
        continue
    if n>0:
        break
answer=random.randint(1,n)
while True:
    try:
        guess=int(input("Guess:"))
    except ValueError:
        continue
    if guess<0:
        continue
    elif guess==answer:
        print("just right")
        break
    elif guess>answer:
        print("too large")
    else:
        print("too small")
