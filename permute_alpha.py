from itertools import permutations


def solve(S, k):
    [print("".join(item)) for item in permutations(sorted(S), k)]


if __name__ == "__main__":
    inputs = input().split()
    S, k = inputs[0], int(inputs[1])

    solve(S, k)