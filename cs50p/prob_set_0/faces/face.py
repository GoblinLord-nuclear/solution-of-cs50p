def main():
    str_1=input()
    str_2=convert(str_1)
    print(str_2)
def convert(string):
    str_2=string.replace(":)","🙂").replace(":(","🙁")
    return str_2
main()