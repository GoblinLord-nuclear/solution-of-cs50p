def main():
    hour,minutes=input("what time is it").strip().split(":")
    minutes,period=minutes.split(" ")
    hour=float(hour)
    minutes=float(minutes)
    convert(hour,minutes,period)
def convert(hour,minutes,period):
    if "p.m" in period:
        hour+=12
    time=(hour*60+minutes)/60
    if 7<=time<=8:
        print("breakfast time")
    elif 12<=time<=13:
        print("lunch time")
    elif 18<=time<=19:
        print("dinner time")
if __name__=="__main__":
    main()
    