from collections import defaultdict


def solve(awords:list, bwords:list):
    d = defaultdict(list)

    for itemB in bwords:
        i = 0
        for itemA in awords:
            if itemA == itemB:
                d[itemB].append(awords.index(itemA, i, len(itemA)))
            i += 1
    for i in range(len(d)):
        print(d[i][1])


if __name__ == "__main__":
    A, B = input().split()
    A, B = int(A), int(B)

    wordsA = []
    wordsB = []

    [wordsA.append(input()) for _ in range(A)]
    [wordsB.append(input()) for _ in range(B)]

    solve(wordsA, wordsB)

