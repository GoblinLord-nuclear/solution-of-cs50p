import inflect
p=inflect.engine()
name_list=[]
while True:
    try:
        name=input("Name:").strip().capitalize()
        name_list.append(name)
    except EOFError:
        break    
print("Adieu, adieu, to "+p.join(name_list))