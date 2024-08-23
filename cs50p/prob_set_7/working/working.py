import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    matches=re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$",s)
    if not matches:
        raise ValueError("didn't found")
    start_hour,start_minute,start_period,end_hour,end_minute,end_period=matches.groups()
    start_hour = int(start_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_hour = int(end_hour)
    end_minute = int(end_minute) if end_minute else 0
    if not ((0<start_hour<=12) and (0<=start_minute<60)):
        print("start_value error")
        raise ValueError("start time valueerror")
    if not ((0<end_hour<=12) and (0<=end_minute<60)):
        print("end_value error")
        raise ValueError("end time valueerror")
    start_time_24=convert_2_24(start_hour,start_minute,start_period)
    end_time_24=convert_2_24(end_hour,end_minute,end_period)

    return(f"{start_time_24} to {end_time_24}")
def convert_2_24(h,m,p):
    if p=="PM":
        if h!=12:
            h+=12
    else:
        if h==12:
            h=0
    return(f"{h:02}:{m:02}")


if __name__ == "__main__":
    main()  