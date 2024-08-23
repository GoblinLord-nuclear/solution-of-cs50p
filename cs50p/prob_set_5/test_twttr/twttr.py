def main():
    word=input("input:")
    shorten_word=shorten(word)
    print(shorten_word)


def shorten(word):
    shorten_word=""
    for c in word:
        if c.lower() in["a","e","i","o","u"]:
            continue
        shorten_word+=c
    return shorten_word


if __name__ == "__main__":
    main()