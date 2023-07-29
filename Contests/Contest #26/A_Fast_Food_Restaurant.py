tc = int(input())

for _ in range(tc):
    dish = list(map(int, input().split()))
    dish.sort(reverse=True)
    total = 0

    if dish[0]:
        total += 1
        dish[0] -= 1
    
    if dish[1]:
        total += 1
        dish[1] -= 1
    
    if dish[2]:
        total += 1
        dish[2] -= 1
    
    if dish[0] and dish[1]:
        total += 1
        dish[0] -= 1
        dish[1] -= 1
    
    if dish[0] and dish[2]:
        total += 1
        dish[0] -= 1
        dish[2] -= 1
    
    if dish[1] and dish[2]:
        total += 1
        dish[1] -= 1
        dish[2] -= 1
    
    if dish[0] and dish[1] and dish[2]:
        total += 1
        dish[0] -= 1
        dish[1] -= 1
        dish[2] -= 1
    
    print(total)
    