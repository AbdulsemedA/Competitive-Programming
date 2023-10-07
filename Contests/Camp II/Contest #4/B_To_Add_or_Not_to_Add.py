def solve(n, k, arr):
    arr.sort()
    prefix = [0]
    maxi = [0,0]

    for i in range(n):
        prefix.append(prefix[-1] + arr[i])

    for i in range(n):
        l, r = 0, i + 1

        while l < r:
            mid = l + (r - l) // 2
            
            if (i + 1 - mid) * arr[i] <= (prefix[i+1] - prefix[mid] + k):
                r = mid
            else:
                l = mid + 1

        if (i + 1 - r) > maxi[0]:
            maxi = [i + 1 - r, arr[i]]

    print(maxi[0], maxi[1])

n, k = map(int, input().split())
arr = list(map(int, input().split()))
solve(n, k, arr)
