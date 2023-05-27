n, m = map(int,input().split())
rep = {i: [i, 0] for i in range(1, n + 1)}

def finder(x):
    while x != rep[x][0]:
        x = rep[x][0] 
    return x

def union(x, y):
    fst = finder(x)
    snd = finder(y)

    if fst != snd:
        if rep[fst][1] <= rep[snd][1]:
            rep[fst][0] = snd
            rep[snd][1] += 1 + rep[fst][1]
        else:
            rep[snd][0] = fst
            rep[fst][1] += 1 + rep[snd][1]

for _ in range(m):
    arr = list(map(int, input().split()))
    size = arr[0]

    if size:
        for i in range(1, len(arr) - 1):
            union(arr[i], arr[i + 1])

ans = [0 for _ in range(n)]

for x in range(1, n + 1):
    ans[x-1] = rep[finder(x)][1] + 1

print(*ans)