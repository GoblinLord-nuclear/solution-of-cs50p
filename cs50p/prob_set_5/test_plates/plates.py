def main():
    s=input("input:")
    print(s)


def is_valid(s):
    return(is_valid_length(s)and start_with_two_letters(s) and no_invalid_charactors(s) and valid_number_placement(s) and no_zero(s))
def is_valid_length(s):
    return 2<=len(s)<=6
def start_with_two_letters(s):
    return s[:2].isalpha()
def no_invalid_charactors(s):
    for ch in s:
        if not ch.isalnum():
            return False
    
    return True
def valid_number_placement(s):
    letters=""
    numbers=""
    for ch in s:
        if ch.isalpha():
            letters="".join([letters,ch])
        else:
            numbers="".join([numbers,ch])
    return s==letters+numbers
def no_zero(s):
    for ch in s:
        if ch.isdigit():
            return ch!="0"
    return True


if __name__ == "__main__":
    main()