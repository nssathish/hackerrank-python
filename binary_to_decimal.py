def binary_to_decimal(binaries: list):
    number = list()
    for binary in binaries:
        decimal_result = 0
        base = 2
        for _ in binary:
            digit = int(_)
            decimal_result += digit * base
            base *= 2
        
        number.append(decimal_result)
    
    return number

if __name__ == "__main__":
    binaries = "01010011 01101111 01100110 01110100 01110111 01100001 01110010 01100101 00100000 01000100 01100101 01110110 01100101 01101100 01101111 01110000 01100101 01110010".split()
    print([chr(number) for number in binary_to_decimal(binaries)])
    