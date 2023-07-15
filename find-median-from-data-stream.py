from sortedcontainers import SortedList
class MedianFinder:
    def __init__(self):
        self.arr = SortedList()

    def addNum(self, num: int) -> None:
        self.arr.add(num)
        
    def findMedian(self) -> float:
        n, mid = len(self.arr), 0
        
        if n % 2: mid = self.arr[n//2]
        else: mid = (self.arr[n // 2 - 1] + self.arr[n // 2]) / 2
        
        return mid

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()