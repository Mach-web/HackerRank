"""
https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
def find_subset(lenA, A, lenB, B):
    myDict = {}
    for i in B:
        myDict[i] = i
    for j in A:
        if j not in myDict:
            return False
            break
        else:
            lenA -= 1
            if lenA == 0:
                return True

if __name__ == "__main__":
    elements = int(input())
    for i in range(elements):
        lenA = int(input())
        A = input().split()
        lenB = int(input())
        B = input().split()
        print(find_subset(lenA, A, lenB, B))
"""
Sample Input
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3 
9 8 2
Sample Output
True
False
False
"""