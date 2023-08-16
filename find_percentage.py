if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores = student_marks[query_name]
    sum_scores = 0
    length = 0
    # Find the average
    for _ in scores:
        sum_scores += _
        length += 1
    avg = sum_scores/length
    # print with 2 decimal places
    print("{:.2f}".format(avg))
