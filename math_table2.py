def print_formatted(num):
    max_indent = len(bin(num).replace('0b', ''))
    
    for number in range(1, num):
        decimal = str(number).rjust(max_indent)
        octal = oct(number).replace("0o", "").rjust(max_indent)
        hexadecimal = hex(number).replace("0x", "").upper().rjust(max_indent)
        # binary = " " * (max_indent - len(bin(number).replace("0b",""))) + bin(number).replace("0b", "")
        binary = bin(number).replace("0b","")
        print(decimal + " " + octal + " " + hexadecimal + " " + binary.rjust(max_indent))

if __name__ == "__main__":
    n = int(input())

    print_formatted(n)