camel_name=input("camel case:")
print("snake case:",end="")
for c in camel_name:
    if c.islower():
        print(c,end="")
    else:
        print("_"+c.lower(),end="")
