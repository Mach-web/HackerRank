if __name__ == "__main__":
    sentence = input("Enter the word: ").lower().replace(" ", "")
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    set_sentence = set()

    for i in sentence:
        set_sentence.add(i)

    for j in alphabets:
        if j not in set_sentence:
            print(False)
            break
    else:
        print(True)

