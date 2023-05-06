class Solution:
    def heapify(self, arr, n, i):
            lrg = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[i]:
                lrg = left
            if right < n and arr[right] > arr[lrg]:
                lrg = right
            
            if lrg != i:
                arr[i], arr[lrg] = arr[lrg], arr[i]
                self.heapify(arr, n, lrg)
        
    def max_heap(self, arr, n):
        for i in range((n // 2 - 1), -1, -1):
            self.heapify(arr, n, i)
        return arr

    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        while n > 1:
            first = heapq.heappop(self.max_heap(stones, n))
            second = heapq.heappop(self.max_heap(stones, n - 1))

            diff = first - second
            n -= 2
            if diff:
                heapq.heappush(stones, diff)
                n += 1
            self.max_heap(stones, n)
        
        return stones[0] if stones else 0