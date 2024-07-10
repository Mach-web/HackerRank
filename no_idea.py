# https://www.hackerrank.com/challenges/no-idea/problem
if __name__ == "__main__":
    n, m = map(int, input().strip().split(" "))
    arr_n = list(map(int, input().strip().split(" ")))
    arr_A = set(map(int, input().strip().split(" ")))
    arr_B = set(map(int, input().strip().split(" ")))
    
    happiness = 0
    for i in arr_n:
        if i in arr_A:
            happiness += 1
        elif i in arr_B:
            happiness -= 1
    print(happiness)
    