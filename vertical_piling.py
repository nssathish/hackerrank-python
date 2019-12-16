# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

def arrange_vertical_pile(cubes: deque):
    result = 'No'
    topcube = None

    if len(cubes) == 1:
        result = 'Yes'
    else:
        while len(cubes) != 0:
            cubei = cubes.popleft()
            cubej = cubes.pop() if len(cubes) > 0 else None

            if cubej != None and cubei != None and topcube == None:
                if cubej >= cubei:
                    topcube = cubei
                    result = 'Yes'
                else:
                    topcube = cubej
                    result = 'Yes'
            elif cubej != None and cubei != None and topcube != None:
                if cubei > topcube or cubej > topcube:
                    result = 'No'
                    break
                
                if cubei >= cubej:
                    topcube = cubej
                    result = 'Yes'
                else:
                    topcube = cubei
                    result = 'Yes'
            elif cubej == None and topcube != None:
                if cubei > topcube:
                    result = 'No'
                    break
                else:
                    topcube = cubei
                    result = 'Yes'
            elif cubei == None and topcube != None:
                if cubej > topcube:
                    result = 'No'
                    break
                else:
                    topcube = cubej
                    result = 'Yes'
            else:
                result = 'No'

    return result

if __name__ == "__main__":
    T = int(input())
    results = list()

    for _ in range(T):
        no_of_cubes = int(input())
        cubes = deque(map(int, input().split()))
        results.append(arrange_vertical_pile(cubes))

    [print(result) for result in results]