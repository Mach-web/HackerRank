"""https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen"""
def check_superset(len_super, superset, set):
    length_set = len(set)
    for _ in set:
        # incase a value is not in the superset, it returns False and breaks the loop
        if _ not in superset:
            return False
            break
        else:
            length_set -= 1
            '''If all values in the set are in the superset, check whether if the last element is in the superset incase the length of set is equal to length of super set'''
            if length_set == 0:
                if len(set) == len_super:
                    if _ in super:
                        return False
                    else:
                        return True
                else:
                    return True
if __name__ == "__main__":
    # input the superset
    super = input().split()
    # find the length of inputs
    len_super = len(super)
    # assign each value to a key and value in dictionary
    superset = {}
    for _ in super:
        superset[_] = _
    # second input
    N = int(input())
    # for each set input, check whether it is a super set and append the results in a results list
    results = []
    for _ in range(N):
        set = input().split()
        results.append(check_superset(len_super, superset, set))

    if False in results:
        print(False)
    else:
        print(True)



