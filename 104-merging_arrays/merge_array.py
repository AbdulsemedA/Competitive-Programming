n, m = map(int,input().split())
arr = list(map(int, input().split(" ")))
arr2 = list(map(int, input().split(" ")))

result = []
i, j = 0, 0

while i < n and j < m:
    if arr[i] <= arr2[j]:
        result.append(arr[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1

if i < n and j == m:
    result.extend(arr[i:])
elif j < m and i == n:
    result.extend(arr2[j:])

print(*result)
