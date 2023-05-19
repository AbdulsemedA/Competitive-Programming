tc = int(input())

for _ in range(tc):
    l, r = map(int, input().split(" "))
    
    if not r % l:
        print(l, r)
    else:
        print(l, r - (r % l))