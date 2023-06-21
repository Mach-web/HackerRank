'''Given a set of non negative integers and a value sum, determine if there is a subset of the given set with sum
 equal to the given sum'''
def find_subset(set, sum):
    if sum == 0:
        return True
    if set == []:
        return False
    else:
        if set[-1] > sum:
            return find_subset(set[:-1], sum)
        else:
            return find_subset(set[:-1], sum) or find_subset(set[:-1], sum - set[-1])

if __name__ == '__main__':
    set = [1, 23, 34, 4, 5, 7, 6]
    sum = int(input())
    print(find_subset(set, sum))
