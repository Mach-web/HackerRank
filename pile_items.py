''' import numpy - was thinking of converting the whole input to an array but that would not be efficient.
There is no need to convert all values to integers yet we would not need to evaluate all of them'''
import sys


def pile_items(length, arr):
    for _ in range(0, length):
        if len(arr) <= 2:
            return 'Yes'
            break
        if arr[-1] > arr[0]:
            if arr[-2] > arr[-1]:
            # Given that the element at the chosen edge was largest, return No if it is smaller than next element
                return 'No'
                break
            else:
            # remove the last element and reduce the length by 1
                arr.pop(-1)

        else:
            if arr[1] > arr[0]:
                return 'No'
                break
            else:
                arr.pop(0)


if __name__ == '__main__':
    inputs = int(input())
    results = []
    for inpt in range(inputs):
        length = int(input())
        arr = list(map(int, input().split()))
        results.append(pile_items(length, arr))
    for result in results:
        print(result)

"""Sample Input
2
6
4 3 2 1 3 4
3
1 3 2
Output
Yes
No
"""
