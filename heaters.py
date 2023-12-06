class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int: 
        dist = {node: float('inf') for node in houses}
        heaters.sort()
        
        for i in houses:
            if i >= heaters[-1]:
                dist[i] = i - heaters[-1]

            elif i <= heaters[0]:
                dist[i] = heaters[0] - i
                
            else:
                idx1 = bisect.bisect_left(heaters, i)
                idx2 = bisect.bisect_right(heaters, i)
                dist[i] = min(abs(heaters[idx1] - i), abs(heaters[idx2 - 1] - i))
        
        return max(dist.values())