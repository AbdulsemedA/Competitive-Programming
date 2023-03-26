class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick(arr, left, right):
            if not arr:
                return []
            elif left == right:
                return [arr[left]]
            else:
                pivot = left + (right - left) // 2
                first = []
                second = []

                for i in range(len(arr)):
                    if i != pivot:
                        if arr[i] <= arr[pivot]:
                            first.append(arr[i])
                        else:
                            second.append(arr[i])
                
                Left = quick(first, 0, len(first) - 1)
                Right = quick(second, 0, len(second) - 1)

                return Left + [arr[pivot]] + Right
        
        return quick(nums, 0, len(nums) - 1)[-k]