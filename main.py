# i = int(input())
# if i < 8:
#     octal = i
# else:
#     myList = [str(i // 8), str(i % 8)]
#     octal = "".join(myLis)
# val = input().split()
# a = int(val[0])
# b = int(val[1])
# if b == 0:
#     raise "Error found"

def hexa(number):
    hexa = []
    while number != 0:
        hexa.append(str(number % 16))
        number = number // 16
    hexa.reverse()
    hexa = list(map(lambda x: "A" if x == "10" else "B" if x == "11" else "C" if x == "12" else "D" if x == "13" else "E" if x == "14" else "F" if x == "15" else x, hexa))
    return "".join(hexa)





