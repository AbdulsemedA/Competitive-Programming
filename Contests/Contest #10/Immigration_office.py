n = int(input())
names = list(input().split())
queries = int(input())
for _ in range(queries):
    new = input()
    left = 0
    right = len(names) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if new > names[mid]:
            left = mid + 1
        elif new < names[mid]:
            right = mid - 1
        else:
            break
    if right < 0:
        print(0)
    elif left == len(names):
        print(len(names))
    else:
        print(left)