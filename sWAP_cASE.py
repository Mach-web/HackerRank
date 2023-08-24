def swap_case(s):
    letter_list = [letter.upper() for letter in s if letter.islower()]
    # for letter in s:
    #     if letter.islower():

    return letter_list
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)