import math 
m, n, k = map(int, input().split())
total = int(math.ceil(m / k) * math.ceil(n / k))
print(total)
