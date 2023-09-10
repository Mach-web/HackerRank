def decimal(n):
    return str(n)
def binary(number):
    bin = []
    while number != 0:
        bin.append(str(number%2))
        number = number//2
    bin.reverse()
    return ''.join(bin)

def octal(number):
    octal = []
    while number != 0:
        octal.append(str(number % 8))
        number = number // 8
    octal.reverse()
    return ''.join(octal)

def hexa(number):
    hexa = []
    while number != 0:
        hexa.append(str(number % 16))
        number = number // 16
    hexa.reverse()
    hexa = list(map(lambda x: "A" if x == "10" else "B" if x == "11" else "C" if x == "12" else "D" if x == "13" else "E" if x == "14" else "F" if x == "15" else x, hexa))
    return "".join(hexa)

def print_formatted(n):
    for i in range(0, n+1):
        print(decimal(i), octal(i), hexa(i), binary(i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)