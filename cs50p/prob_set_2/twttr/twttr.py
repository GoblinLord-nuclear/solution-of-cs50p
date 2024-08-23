word=input("Input:")

for c in word:
    if c.lower() in["a","e","i","o","u"]:
        continue
    print(c,end="")