from operator import itemgetter
from itertools import groupby

#First class function that takes 
#anoher function as an argument
def person_lister(f):
    def inner(people):
        people.sort(key=itemgetter(2))
        result = list()
        for age,persons in groupby(people, itemgetter(2)):
            for person in persons:
                result.append(("Mr. " if person[3] == "M" else "Ms. ") +  person[0] + " " + person[1])
        return result

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") +  person[0] + " " + person[1]

if __name__ == "__main__":
    people = list()
    for i in range(int(input())):
        item = input().split()
        item[2] = int(item[2])
        people.append(item)
        
    print(*name_format(people), sep='\n')