'''https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true'''
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr, reverse = True)
    i = 0
    while arr[i] == arr[i+1]:
        i += 1
    print(arr[i+1])