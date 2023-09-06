if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        val = input().split()

        try:
            a = int(val[0])
            b = int(val[1])
            print(a/b)
        except ZeroDivisionError as e:
            print(f'Error Code: {e}')
        except ValueError as e:
            print("Error Code: ", e)
