'''
https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
'''
def swap_case(s):
    letter_list = [letter.lower() if letter.isupper() else letter.upper() for letter in s]
    # Join the list to a sr=tring
    return ''.join(letter_list)

if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
