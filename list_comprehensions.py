# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

def list_comprehensions(x, y, z, n):
    output = list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                item_list = [i, j, k]
                if sum(item_list) == n:
                    pass
                else:
                    output.append(item_list)
    return output       

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list_comprehensions(x, y, z, n))