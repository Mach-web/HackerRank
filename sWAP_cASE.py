def swap_case(s):
    letter_list = [letter.lower() if letter.isupper() else letter.upper() for letter in s]
    return ''.join(letter_list)

if "__main__" == __name__:
    s = input()
    result = swap_case(s)
    print(result)
