def solve(n, m):
    dash = '-'
    dot_pipe = '.|.'
    welcome = 'WELCOME'
    welcome_length = len(welcome)
    first_half = list()

    #Top of the rombhus
    for i in range(1, n, 2):
        print_dot_pipe = dot_pipe * i
        print_dash = dash * ((m - len(print_dot_pipe)) // 2)

        line_item = print_dash + print_dot_pipe + print_dash
        first_half.append(line_item)
        print(line_item)
    
    #Print WELCOME
    print_dash = dash * ((m - welcome_length) // 2)
    print( print_dash + welcome + print_dash )

    for i in range(len(first_half) - 1, -1, -1 ):
        print(first_half[i])


if __name__ == "__main__":
    n, m = input().split()
    rows = int(n)
    cols = int(m)

    solve(rows, cols)
