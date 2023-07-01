def check_superset(superset, set):
    length_set = len(set)
    for _ in set:
        if _ not in superset:
            return False
            break
        else:
            length_set -= 1
            if length_set == 0:
                if len(set) == len(superset):
                    if _ in super:
                        return False
                    else:
                        return True
                else:
                    return True
if __name__ == "__main__":
    super = input().split()
    superset = {}
    for _ in super:
        superset[_] = _
    N = int(input())
    results = []
    for _ in range(N):
        set = input().split()
        results.append(check_superset(superset, set))
    for _ in results:
        if _ == False:
            print(False)
            break
        if _ == results[-1]:
            print(True)



