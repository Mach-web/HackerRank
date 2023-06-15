# Enter your code here. Read input from STDIN. Prin
len_nm =input()

len_n = int(len_nm.split()[0])
len_m = int(len_nm.split()[1])

# for i in range(0, 3):
n = input()
n = [int(i) for i in n.split()]

mA = input()
mA = [int(i) for i in mA.split()]

mB = input()
mB = [int(i) for i in mB.split()]
points = 0

for i in mA:
    if i in n:
        points += 1
for i in mB:
    if i in n:
        points -= 1
print(points)

"""3 2
1 5 3
3 1
5 7"""