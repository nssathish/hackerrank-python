class if_else_problem:
    def __init__(self, n):
        self.n = n

    def solve(self):
        if self.n % 2 != 0:
            print('Weird')
            a = 1
            b = 2
            print(f'{a + b}')


if __name__ == '__main__':
    prob = if_else_problem(5)
    prob.solve()