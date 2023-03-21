n, m = map(int, input().split())
prefix = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    prefix[a] += 1
    prefix[b+1] -= 1
    
prefix.pop()
prev = 0
exist = "NO"

for i in range(n):
    prefix[i] += prev
    prev = prefix[i]
    if prefix[i] == 0:
        exist = "YES"
        break

print(exist)