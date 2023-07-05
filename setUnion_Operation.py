if __name__ == "__main__":
    len_english = int(input())
    english = set(input().split())
    len_french = int(input())
    french = set(input().split())
    print(len(english.union(french)))
