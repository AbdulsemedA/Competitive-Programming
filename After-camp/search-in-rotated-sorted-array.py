class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        new_left = new_right = 0
        mids = set()
        
        if n == 1:
            return 0 if nums[0] == target else -1

        if nums[0] > nums[-1]:
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid + 1] < nums[mid]:
                    new_left = mid + 1
                    new_right = mid
                    break
                else:
                    if nums[left] > nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            left, right = new_left, new_right
            
            while left != right:
                mid = left + (right - left) // 2
                if mid in mids: return -1
                mids.add(mid)

                if nums[left] < nums[right] and left > right:
                    mid = (left + (n - left + right) // 2) % n
                    
                if nums[mid] == target:
                    return mid

                elif nums[mid] < target:
                    left = (mid + 1) % n

                else:
                    if not mid:
                        right = n - 1
                    else:
                        right = (mid - 1) % n

            if nums[left] == target: return left
        else:
            left = 0
            right = n - 1
            x = target
        
            while left <= right:
                mid = (right + left) // 2
        
                if nums[mid] < x:
                    left = mid + 1
        
                elif nums[mid] > x:
                    right = mid - 1
        
                else:
                    return mid
        
        return -1