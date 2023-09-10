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

print(2//8)
print(2%8)
def octal(number):
    octal = []
    while number != 0:
        octal.append(str(number % 8))
        number = number // 8
    octal.reverse()
    return ''.join(octal)
print(octal(14))
