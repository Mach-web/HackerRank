if __name__ == '__main__':
    s = input()
    length = len(s)
    leng = 0
    for i in s:
        if i.isalnum():
            print(True)
            break
        else:
            leng += 1
            if leng == length:
                print(False)
    leng = 0
    for i in s:
        if i.isalpha():
            print(True)
            break
        else:
            leng += 1
            if leng == length:
                print(False)
    leng = 0
    for i in s:
        if i.isdigit():
            print(True)
            break
        else:
            leng += 1
            if leng == length:
                print(False)
    leng = 0
    for i in s:
        if i.islower():
            print(True)
            break
        else:
            leng += 1
            if leng == length:
                print(False)
    leng = 0
    for i in s:
        if i.isupper():
            print(True)
            break
        else:
            leng += 1
            if leng == length:
                print(False)