def find_iterables(length, elements, indices):
    list_of_tuples = []
    # indices -= 1
    for i in range(len(elements)):
        j = i
        try:
            while elements[j+indices]:
                list_of_tuples = tuple(elements[j])
                j += 1
                print(list_of_tuples)
        except:
            pass

if __name__ == "__main__":
    length = int(input())
    elements = list(map(lambda x: x, input().split()))
    indices = int(input())
    find_iterables(length, elements, indices)