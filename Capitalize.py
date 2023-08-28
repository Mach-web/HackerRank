"""
https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
"""
def solve(s):
    # print(s.split(" "))
    capitalized_s = []
    # one has to account for the case of several spaces
    for i in s.split(" "):
        capitalized_s.append(i.capitalize())
    # print(capitalized_s)
    return " ".join(capitalized_s)

if __name__ == "__main__":
    s = input()
    result = solve(s)
    print(result)