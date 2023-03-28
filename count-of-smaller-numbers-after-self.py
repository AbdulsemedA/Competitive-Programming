class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.ans = [0] * len(nums)
        
        def merge(a1, a2):
            l1 = l2 = 0
            while l1 < len(a1):
                left, right = l2, len(a2) - 1

                while left <= right:
                    mid = left + (right - left) // 2
                    if a1[l1][0] > a2[mid][0]:
                        left = mid + 1
                    else:
                        right = mid - 1
                self.ans[a1[l1][1]] += left
                l2 = left
                l1 += 1
    
            l1 = l2 = 0
            res = []
            while l1 < len(a1) or l2 < len(a2):
                num1, idx1 = a1[l1] if l1 < len(a1) else (float('inf'), 0)
                num2, idx2 = a2[l2] if l2 < len(a2) else (float('inf'), 0)
                if num1 <= num2:
                    res.append((num1, idx1))
                    l1 += 1
                else:
                    res.append((num2, idx2))
                    l2 += 1
            return res

        def merge_sort(nums, left, right):
            if left == right:
                return [nums[left]]
            mid = left + (right - left) // 2
            left = merge_sort(nums, left, mid)
            right = merge_sort(nums, mid + 1, right)

            return merge(left, right)

        inputs = [(nums[i], i) for i in range(len(nums))]
        res = merge_sort(inputs, 0, len(inputs) - 1)
        # res.sort(key = lambda x: x[1])
        return self.ans