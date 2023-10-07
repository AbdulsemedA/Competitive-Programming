n = int(input())
capacity = {}
curr = space = 0

for _ in range(n):
    do, id = map(str, input().split())
    
    if do == '-':
        if id not in capacity:
            curr += 1
        else:
            space -= 1
    else:
        capacity[id] = 1
        space += 1

        if space > curr:
            curr = space
    
print(curr)