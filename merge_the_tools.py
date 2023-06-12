def merge_the_tools(string, k):
    # your code goes here
    start = 0
    end = k

    while string[start: end]:
        substring = string[start:end]
        values = ""

        for i in substring:
            if i not in values:
                values += i

        start += k
        end += k
        print(values, end = "\n")


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)