#!/bin/python3
from operator import itemgetter
from collections import deque


def solve(s):
    dictionary = dict()
    dq = deque()
    result = list()

    for char in s:
        if dictionary.get(char) is None:
            dictionary[char] = 1
        else:
            existing_count = dictionary.get(char)
            dictionary[char] = existing_count + 1

    items = list()
    for key in dictionary.keys():
        items.append([key, dictionary.get(key)])

    items.sort(key=itemgetter(1), reverse=True)

    items_count = len(items)

    for i in range(items_count):
        if items[i][1] > items[i+1][1]:
            result.append([items[i]])

if __name__ == "__main__":
    s = input()
    solve(s)
