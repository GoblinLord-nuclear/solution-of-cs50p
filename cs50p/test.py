import re
a=input("input")
matches=re.search(r"^(\d{1,2}):?(\d{2})? (AM|pm) to (\d{1,2}):?(\d{2})? (AM|PM)$",a)
sh,sm,sp,eh,em,ep=matches.groups()
print(sm)
print(sp)