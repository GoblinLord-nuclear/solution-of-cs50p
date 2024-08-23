months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
while True:
    try:
        date=input("Date:").strip()
        if len(date.split("/"))==3:
            month,day,year=map(int,date.split("/"))
            
            if month<1 or month >12:
                raise ValueError
        else:
            month_day,year=date.split(",")
            year=year.strip()
            month,day=month_day.split(" ")
            year,day=int(year),int(day)
            if month not in months:
                raise ValueError
            month=int(months.index(month)+1)
        if day>31:
            raise ValueError
        print(f"{year:02}-{month:02}-{day:02}")
    except ValueError:
        print("you should input correct date: month-day-year")
    except EOFError:
        break
    
    
  