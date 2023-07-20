class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.k = k
        track = nums[:]
        
        if len(nums) > k:
            track = nums[len(nums)-k:]
        
        self.track = track
        
    def add(self, val: int) -> int:
        heapq.heappush(self.track, val)

        if len(self.track) > self.k:
            heapq.heappop(self.track)

        return self.track[0] if self.track else 0
  
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)