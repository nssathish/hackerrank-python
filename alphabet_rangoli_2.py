def dash_pad(string, pattern):
    dash_count = len(string) - len(pattern)
    dash = "-" * (dash_count // 2)
    
    return dash + pattern + dash

def solve(n):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
    
    range_to_work = alphabets[0:n]

    one_half = list()

    for i in range(n):
        first_half = range_to_work[i:]
        second_half = first_half[1:]
        if i != n - 1:
            pattern = "-".join(reversed(first_half)) + "-" + "-".join(second_half)
        else:
            pattern = first_half[0]
        
        if len(one_half) > 0:
            pattern = dash_pad(one_half[i-1], pattern)

        one_half.append(pattern)
    
    [print(item) for item in reversed(one_half)]
    [print(item) for item in one_half[1:]]
        
    

if __name__ == "__main__":
    n = int(input())

    solve(n)