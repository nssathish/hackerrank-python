def solve(s):
    result = ""
    string = ""
    i = 0
    if len(s.split()) == 1:
        return s.capitalize

    while i < len(s):
        char = s[i]
        if char == ' ':
            string += char
            while s[i+1] == ' ' and (i + 1) < len(s):
                string += s[i+1]
                i += 1
            result += string.capitalize()
            string = ""
        else:
            string += char

        if (i + 1) == len(s):
            result += string.capitalize()
        
        i += 1
    
    return result
if __name__ == "__main__":
    print(solve(input()))

