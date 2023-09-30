q = int(input())
handles = {}

for _ in range(q):
    old, new = input().split()
    if old not in handles:
        handles[new] = old
    else:
        handles[new] = handles[old]
        del handles[old]

print(len(handles))
for new, old in handles.items():
    print(old, new)