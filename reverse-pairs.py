class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        def check_pairs(arr1, arr2):
            nonlocal count

            if arr1 and arr2:
                tm1 = sorted(arr1)
                tm2 = sorted(arr2)
                cur_idx = 0
                
                for i in range(len(tm1)):
                    left, right = cur_idx, len(tm2) - 1
                    while left <= right:
                        mid = left + (right - left) // 2
                        if tm1[i] <= 2 * tm2[mid]:
                            right = mid - 1
                        else:
                            left = mid + 1
                    count += left
                    if left == len(arr2):
                        count += (len(arr2) * (len(arr1) - (i + 1)))
                        break
                    cur_idx = left

        def divide(arr):
            if len(arr) <= 1:
                return
            mid = len(arr) // 2
            divide(arr[:mid])
            divide(arr[mid:])
            check_pairs(arr[:mid], arr[mid:])
            
        divide(nums)
        return count