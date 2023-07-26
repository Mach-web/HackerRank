'''
https://www.hackerrank.com/challenges/nested-list/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''
if __name__ == '__main__':
    scores = []
    lowest = 1e10
    second_lowest = 1e10
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # append inputs to a list
        scores.append([name, score])

    # loop over the loop to identify the lowest array
    for _ in scores:
        if _[1] < lowest:
            lowest = _[1]
            low_arr = _
    # loop over the loop to identify the second lowest array
    for _ in scores:
        if _[1] > lowest:
            if _[1] < second_lowest:
                second_lowest = _[1]
                second_arr = _
    # incase a value is equal to second lowest in the list, append its name to a list
    arr = []
    for _ in scores:
        if _[1] == second_lowest:
            arr.append(_[0])
    # sort the array of names
    arr = sorted(arr)
    # print out the names
    for _ in arr:
        print(_)













