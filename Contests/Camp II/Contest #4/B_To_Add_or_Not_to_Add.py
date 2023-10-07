from collections import defaultdict

def solve(n, k, arr):
    arr.sort()
    prefix = [0]

    for i in range(n):
        prefix.append(prefix[-1] + arr[i])

    maxi = [1, arr[0]]

    if k == 0:
        hMap = defaultdict(int)
        for i in arr:
            hMap[i] += 1
    
        for i in hMap:
            if hMap[i] > maxi[0]:
                maxi = [hMap[i], i]
            elif hMap[i] == maxi[0]:
                maxi[1] = min(maxi[1], i)

    else:
        for i in range(1, n):
            l = 0
            r = i + 1

            while l < r:
                mid = l + (r - l) // 2

                if (i + 1 - mid) * arr[i] == (prefix[i+1] - prefix[mid] + k):
                    l = r = mid
                    break

                elif (i + 1 - mid) * arr[i] < (prefix[i+1] - prefix[mid] + k):
                    r = mid
                
                else:
                    l = mid + 1

            if (i + 1 - r) > maxi[0]:
                maxi = [i + 1 - r, arr[i]]

    print(maxi[0], maxi[1])

n, k = map(int, input().split())
arr = list(map(int, input().split()))
solve(n, k, arr)
