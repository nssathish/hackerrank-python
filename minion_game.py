def minion_game(string):
    vowels = ['a','e','i','o','u']
    stuart = 0
    kevin = 0
    count = len(string)

    for i in range(count):
        if string[i] in vowels:
            kevin += (count - i)
        else:
            stuart += (count - i)
    
    print(f'Kevin = {kevin} and Stuart = {stuart}')
    print(f'Kevin {kevin}') if kevin > stuart else print(f'Stuart {stuart}')
    
    '''
    BANANA = BA, BAN, BANA, BANAN, BANANA, NA, NAN, NANA 
             AN, ANA, ANAN, ANANA, AN
    
    BANANAN = BA, BAN, BANA, BANAN, BANANA, BANANAN

    '''
if __name__ == '__main__':
    s = input()
    minion_game(s)