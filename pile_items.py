''' import numpy - was thinking of converting the whole input to an array but that would not be efficient.
There is no need to convert all values to integers yet we would not need to evaluate all of them'''
def pile_items(arr):
    # an array can definitely form a stack if it has 2 elements
    if len(arr) == 2:
        return 'Yes'

    if int(arr[-1]) > int(arr[0]):
        if int(arr[-2]) > int(arr[-1]):
            # Given that the element at the chosen edge was largest, return No if it is smaller than next element
            return 'No'
        else:
            # concat the list to remove the chosen element then perform a recursion.
            arr = arr[:-1]
            return pile_items(arr)

    elif int(arr[0]) >= int(arr[-1]):
        if int(arr[1]) > int(arr[0]):
            return 'No'
        else:
            arr = arr[1:]
            return pile_items(arr)


if __name__ == '__main__':
    inputs = int(input())
    list_of_results = []
    for inpt in range(inputs):
        length = int(input())
        arr = input().split()
        list_of_results.append(pile_items(arr))
    for result in list_of_results:
        print(result, end = '\n')
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