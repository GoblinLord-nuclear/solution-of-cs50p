grocery_list={}
while True:
    try:
        item=input().strip().upper()
        if item not in grocery_list:
            grocery_list[item]=1
        else:
            grocery_list[item]+=1
    except EOFError:
        for key,value in sorted(grocery_list.items()):
            print(f"{value} {key}")
        break
