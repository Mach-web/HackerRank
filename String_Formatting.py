def print_formatted(number):
    if number != 1:
        print_formatted(number // 2)

    print(number % 2)
def convert_to_hexa(s):
    if s == 10:
        return "A"
    elif s == 11:
        return "B"
    elif s == 12:
        return "C"
    elif s == 13:
        return "D"
    elif s == 14:
        return "E"
    else:
        return "F"

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)