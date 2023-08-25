def solve(s):
    capitalized_s = []
    for i in s.split():
        capitalized_s.append(i.capitalize())
    return " ".join(capitalized_s)

if __name__ == "__main__":
    s = input()
    result = solve(s)
    print(result)