tc = int(input())

for _ in range(tc):
    n = int(input())
    students = []
    assistants = 1
    
    for _ in range(n):
        students.append(list(map(int, input().split())))

    students.sort(key = lambda x: x[0])
    end = [students[0][1]]

    for i in range(1, n):
        if students[i][0] >= min(end):
            end.remove(min(end))
        else:
            assistants += 1
        end.append(students[i][1])
    
    print(assistants)