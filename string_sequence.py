def merge_the_tools(string, k):
    dictionary = dict()
    result = ""
    counter = 0

    for char in string:
        if dictionary.get(char) == None:
            dictionary[char] = char
            result += char
        counter += 1

        if counter % k == 0:
            print(result)
            dictionary = dict()
            result = ""

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)