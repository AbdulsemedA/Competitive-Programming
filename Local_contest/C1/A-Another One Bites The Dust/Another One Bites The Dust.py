def maximum(lists):
    result = 0
    if lists[0] == lists[1]:
        result = 2 * lists[0] + 2 * lists[2]
    else:
        mini = min(lists[0],lists[1])
        result = 2 * lists[2] + 2 * mini + 1
    
    print(result)

mylist = list(map(int, input().split()))
maximum(mylist)
