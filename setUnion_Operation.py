"""https://www.hackerrank.com/challenges/py-set-union/problem?h_r=next-challenge&h_v=zen"""
if __name__ == "__main__":
    len_english = int(input())
    english = set(input().split())

    len_french = int(input())
    french = set(input().split())
    # perform a union and output the results
    print(len(english.union(french)))
