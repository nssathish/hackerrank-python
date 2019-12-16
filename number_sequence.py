def find_exponent(number):
    no_of_digits = 0

    while number != 0:
        number //= 10
        no_of_digits += 1
    
    return no_of_digits

def solve(n):
    if n <= 1:
        return n
    
    result = 1
    for _ in range (2,n + 1):
        exponent = find_exponent(_)
        result = (result * (10 ** exponent)) + _

    return result

if __name__ == '__main__':
    n = int(input())
    print(solve(n))