def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    length = len(string)
    cons = 0
    vowel = 0
    for i in range(length):
        if string[i] in vowels:
            vowel += (length-i)
        else:
            cons += (length - i)
    if vowel < cons:
        print(f"Stuart {cons}")
    elif vowel > cons:
        print(f"Kevin {vowel}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)