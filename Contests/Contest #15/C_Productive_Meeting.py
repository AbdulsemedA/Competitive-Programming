import heapq
tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [(-arr[i], i + 1) for i in range(len(arr))]
    heapq.heapify(arr)
    pairs = []
    
    while len(arr) > 1:
        first, idx1 = heapq.heappop(arr)
        second, idx2 = heapq.heappop(arr)

        if first and second:
            pairs.append((idx1, idx2))
            first += 1
            second += 1
        
        if first: heapq.heappush(arr, (first, idx1))
        if second: heapq.heappush(arr, (second, idx2))
    
    print(len(pairs))
    for x, y in pairs:
        print(x, y)
        