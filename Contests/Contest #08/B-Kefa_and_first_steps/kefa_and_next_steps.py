n = int(input())
num = list(map(int, input().split(" ")))

maxi, counter = 0, 1

for i in range(n-1):
    if num[i] <= num[i+1]:
        counter += 1
    else:
        maxi = max(maxi, counter)
        counter = 1

maxi = max(maxi, counter)

print(maxi)