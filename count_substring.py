def count_substring(string, sub_string):
    count = 0
    len_sub = len(sub_string)
    for index in range(len(string)):
        if string[index] == sub_string[0]:
            if string[index: index+len_sub] == sub_string:
                count += 1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)