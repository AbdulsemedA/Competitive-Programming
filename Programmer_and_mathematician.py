tc = int(input())

for _ in range(tc):
    a, b = map(int, input().split())
    print(min(a,b,(a+b)//4))
