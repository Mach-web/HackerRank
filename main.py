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
# print(a/b)

def decimal(number):
    binary = []
    while number != 0:
        binary.append(str(number%2))
        number = number//2
    binary.reverse()
    return ''.join(binary)
