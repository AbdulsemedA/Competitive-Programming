x = int(input())
ans = 0

while x > 0:
    d = 1
    count = 1

    while d <= x:
        d *= 2
    
    x -=  d // 2
    ans += count

print(ans)