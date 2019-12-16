def solve(students):
    scores =  [student[1] for student in students]
    second_lowest_grade = get_second_lowest_grade(scores)
    [print(student[0]) for student in sorted(students) if student[1] == second_lowest_grade]

def get_second_lowest_grade(scores):
    lowest = scores[0]
    second_lowest = scores[1]

    if len(scores) == 2 and lowest > second_lowest:
        lowest, second_lowest = second_lowest, lowest
    else:
        for score in scores[2:]:
            if score < lowest:
                lowest, second_lowest = score, lowest
            if score != lowest and (score > lowest and score < second_lowest):
                second_lowest = score

    return second_lowest

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name,score])
    
    solve(students)