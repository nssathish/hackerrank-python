#!/bin/python3
from operator import itemgetter


def solve(s):
    dictionary = dict()
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

    print(items)
    max_range = 0
    result = []
    next_alpha = None
    next_count = None

    for i in range(items_count):
        current_alpha = items[i][0]
        current_count = items[i][1]

        if (i + 1) < items_count:
            if next_alpha is None and next_count is None:
                next_alpha = items[i+1][0]
                next_count = items[i+1][1]

            if current_count == next_count:
                if ord(current_alpha) > ord(next_alpha):
                    current_alpha, current_count, next_alpha, next_count = next_alpha, next_count, current_alpha, current_count
                else:
                    result.append([current_alpha, current_count])
                    max_range += 1
            else:
                result.append([current_alpha, current_count])
                max_range += 1
        else:
            result.append([current_alpha, current_count])
            max_range += 1
        
        if max_range == 3:
            break


if __name__ == '__main__':
    s = input()
    solve(s)
