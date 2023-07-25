if __name__ == '__main__':
    scores = []
    lowest = 1e10
    second_lowest = 1e10
    low = ['a', 1e10]
    second_low = ['b', 1e10]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < lowest:
            second_lowest = lowest
            second_low = low
            lowest = score
            low = [name, score]
        elif score == lowest:
            if name < low[0]:
                second_lowest = lowest
                second_low = low
                lowest = score
                low = [name, score]
            else:
                second_lowest = score
                second_low = [name, score]
        elif score > lowest:
            if score < second_lowest:
                second_lowest = score
                second_low = [name, score]
            elif score == second_lowest:
                if name > second_low[0]:
                    second_lowest = score
                    second_low = [name, score]
    print(f'{low}, {second_low}')










