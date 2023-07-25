if __name__ == '__main__':
    scores = []
    lowest = 1e10
    second_lowest = 1e10
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])

    for _ in scores:
        if _[1] < lowest:
            lowest = _[1]
            low_arr = _

    for _ in scores:
        if _[1] > lowest:
            if _[1] < second_lowest:
                second_lowest = _[1]
                second_arr = _
    arr = []
    for _ in scores:
        if _[1] == second_lowest:
            arr.append(_[0])

    arr = sorted(arr)
    for _ in arr:
        print(_)













