tc = int(input())

for _ in range(tc):
    n, t = map(int, input().split())
    durations = list(map(int, input().split()))
    entertain = list(map(int, input().split()))

    idx = -1
    for i in range(n):
        if i + durations[i] <= t:
            if idx < 0 or entertain[idx] < entertain[i]:
                idx = i

    print(idx + 1 if idx > -1 else -1)