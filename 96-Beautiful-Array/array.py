def beauty_array(lists):
    answer = [[0],[0],[0]]
    for item in lists:
        if item == 0:
            answer[2].append(item)
            answer[2][0] += 1 
        elif item < 0:
            answer[0].append(item)
            answer[0][0] += 1
        else:
            answer[1].append(item)
            answer[1][0] += 1

    if answer[1][0] == 0:
        for _ in range(2):
            answer[1].append(answer[0][-1])
            answer[0][0] -= 1
            answer[1][0] += 1
            answer[0].pop()

    if answer[0][0] % 2 == 0:
        answer[2].append(answer[0][-1])
        answer[0].pop()
        answer[0][0] -= 1
        answer[2][0] += 1

    for item in answer:
        print(" ".join([str(ch) for ch in item]))
    
size = int(input())
mylist = list(map(int,input().split()))
beauty_array(mylist)
    
