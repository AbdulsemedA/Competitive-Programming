n, t = map(int, input().split())
portals = list(map(int, input().split()))
idx = 0

while idx < t:
    idx += portals[idx]
    if idx == t - 1:
        print("YES")
        break
    elif idx > t - 1:
        print("NO")
        break