from enum import Enum
class Operation(Enum):
    INSERT = 'insert'
    REMOVE = 'remove'
    APPEND = 'append'
    SORT = 'sort'
    POP = 'pop'
    REVERSE = 'reverse'
    PRINT = 'print'


class NewList:
    def __init__(self):
        self.integer_list = list()

    def __str__(self):
        return f"[{', '.join([str(list_item) for list_item in self.integer_list])}]"

    def append(self, element):
        self.integer_list.append(element)

    def insert(self, position, element):
        self.integer_list.insert(position, element)

    def remove(self, element):
        self.integer_list.remove(element)
    
    def pop(self):
        self.integer_list.pop()
    
    def reverse(self):
        self.integer_list.reverse()

    def sort(self):
        self.integer_list.sort()

if __name__ == '__main__':
    N = int(input())

    new_list = NewList()

    for _ in range(N):
        operation, *args = input().split()
        
        if operation == Operation.INSERT.value:
            new_list.insert(int(args[0]), int(args[1]))
        elif operation == Operation.REMOVE.value:
            new_list.remove(int(args[0]))
        elif operation == Operation.APPEND.value:
            new_list.append(int(args[0]))
        elif operation == Operation.POP.value:
            new_list.pop()
        elif operation == Operation.PRINT.value:
            print(new_list)
        elif operation == Operation.REVERSE.value:
            new_list.reverse()
        elif operation == Operation.SORT.value:
            new_list.sort()
