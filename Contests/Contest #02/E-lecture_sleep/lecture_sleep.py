def lecture_sleep(value,status,n,k):
    stack = []
    result = total = current = 0
    
    for item in range(n):
        if status[item] == 1:
            result += value[item]
    
    for item in range(n):
        if status[item] != 0:
            stack.append(0)
        else:
            stack.append(value[item])
            current += value[item]
        
        if len(stack) == k:
            total = max(total,current + result)
            current -= stack[0]
            stack.pop(0)
                
    print(total)
    
n, k = map(int, input().split(" "))
value = list(map(int, input().split()))
status = list(map(int, input().split()))

lecture_sleep(value,status,n,k)
