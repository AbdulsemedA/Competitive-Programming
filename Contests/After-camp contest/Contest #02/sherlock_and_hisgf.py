n = int(input())
check = [1] * (n)
i = 2

while i * i <= n + 1:
    if check[i - 2] == 1:
        j = i * i
        
        while j <= n + 1:
            check[j - 2] = 2
            j += i
    i += 1
    
print(len(set(check)))
print(*check)