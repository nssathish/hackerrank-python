def count_substring(string, sub_string):
    if len(string) == 1:
        if len(string) == len(sub_string) and \
        string[0] == sub_string[0]:
            return 1
        else:
            return 0
    elif len(string) < len(sub_string):
        return 0
    elif len(string) == len(sub_string):
        if string == sub_string:
            return 1
        else:
            return 0
    else:
        count = 0
        sub_string_index = 0
        for i in range(len(string)):
            char = string[i]
            index = i
            found = False
            sub_string_index = 0
            if char == sub_string[0]:
                sub_string_index = 1
                if len(sub_string) == 1:
                    found = True
                for j in range(1, len(sub_string)):
                    sub_char = sub_string[j]
                    if index + 1 < len(string):
                        if string[index + 1] == sub_char:
                            sub_string_index += 1
                            found = True
                            index += 1
                        else:
                            found = False
                            break
                    j += 1

            if found and sub_string_index + 1 == len(sub_string):
                count += 1

        return count

def count_substring_using_str_find(string, sub_string):
    return string.count(sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    # count = count_substring(string, sub_string)
    count = count_substring_using_str_find(string, sub_string)
    print(count)