class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n, idx, curr = len(heights), 1, 0
        heap = []
        
        while idx < n:
            diff = heights[idx] - heights[idx - 1]

            if diff > 0:
                heapq.heappush(heap, -diff)
                curr += diff

                if curr > bricks:
                    if ladders:
                        curr += heapq.heappop(heap)
                        ladders -= 1
                    else:
                        return idx - 1
            
            idx += 1
    
        return idx - 1