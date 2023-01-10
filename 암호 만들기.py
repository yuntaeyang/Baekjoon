from itertools import combinations

def main():
    L, C = map(int,input().split())
    alpha = sorted(input().split())
    words = combinations(alpha, L)

    for string in words:
        moem = 0
        jaem = 0
        for i in string:
            if i in ["a", "e", "i" , "o", "u"]:
                moem += 1
            else:
                jaem += 1
        if (moem > 0) & (jaem > 1):
            print("".join(string))

if __name__ == "__main__":
    main()