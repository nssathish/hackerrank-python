def print_formatted(number):
    
    result = ""
    for i in range(1, number):
        result = format_output(str(i) + get_octal(i) + get_hex(i) + get_bin(i))
        print(result)

def get_octal(number):
    base = 8
    result = ""
    while(number):
        result += "0" if number % base == 0 else "1"
        number //= base

    return result    

def get_hex(number):
    pass

def get_bin(number):
    pass

def format_output(string):
    return string

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)