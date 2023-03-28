n, k = map(int, input().split())
arr = list(map(int, input().split()))
players = [(arr[i], i) for i in range(2**n)]

def merge(a1, a2):
    l1 = l2 = 0
    new_arr = []

    while l1 < len(a1) or l2 < len(a2):
        num1, idx1 = a1[l1] if l1 < len(a1) else (float('inf'), idx1)
        num2, idx2 = a2[l2] if l2 < len(a2) else (float('inf'), idx2)
        if num1 <= num2:
            if a2[0][0] - k <= num1: new_arr.append(tuple([num1, idx1]))
            l1 += 1
        else:
            if a1[0][0] - k <= num2: new_arr.append(tuple([num2, idx2]))
            l2 += 1

    return new_arr

def mergeSort(players):
    if len(players) <= 1:
        return players
    mid = len(players) // 2
    left = mergeSort(players[:mid])
    right = mergeSort(players[mid:])
    return merge(left, right)

winner = mergeSort(players)
print(*([i[1] + 1 for i in sorted(winner, key = lambda x: x[1])]))
