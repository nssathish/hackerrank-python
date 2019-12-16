import re

def isAlphaNumeric(string):
    # pattern = re.compile('[a-zA-Z0-9]+|[a-z]+[A-Z]+[0-9]+|[a-z]+[0-9]+[A-Z]+|[A-Z]+[a-z]+[0-9]+|[A-Z]+[0-9]+[a-z]+|[0-9]+[A-Z]+[a-z]+|[0-9]+[a-z]+[A-Z]+')
    # return pattern.findall(string)
    print(string.isalnum())

def isAlphabet(string):
    # pattern = re.compile('[a-zA-Z]+')
    # return pattern.findall(string)

    print(string.isalpha())

def isDigit(string):
    # pattern = re.compile('[0-9]')
    # return pattern.findall(string)

    print(string.isdigit())

def isLower(string):
    # pattern = re.compile('[a-z]')
    # return pattern.findall(string)
    print(string.islower())

def isUpper(string):
    # pattern = re.compile('[A-Z]')
    # return pattern.findall(string)
    print(string.isupper())

if __name__ == '__main__':
    S = input()
    isAlphaNumeric(S)
    isAlphabet(S)
    isDigit(S)
    isLower(S)
    isUpper(S)
    # print('True') if isAlphaNumeric(S) else print('False')
    # print('True') if isAlphabet(S) else print('False')
    # print('True') if isDigit(S) else print('False')
    # print('True') if isLower(S) else print('False')
    # print('True') if isUpper(S) else print('False')
