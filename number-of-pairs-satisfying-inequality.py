class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        dif = [nums1[i] - nums2[i] for i in range(len(nums1))]
        self.diff = diff
        self.count = 0
        
        def merge(a1, a2):
            l1 = l2 = 0
            while l1 < len(a1):
                left, right = l2, len(a2) - 1

                while left <= right:
                    mid = left + (right - left) // 2

                    if a1[l1] - self.diff > a2[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                self.count += len(a2) - left
                l1 += 1
                l2 = left

            ans = []
            l1 = l2 = 0
            while l1 < len(a1) or l2 < len(a2):
                n1 = a1[l1] if l1 < len(a1) else float("inf")
                n2 = a2[l2] if l2 < len(a2) else float("inf")
                if n1 <= n2:
                    ans.append(n1)
                    l1 += 1
                else:
                    ans.append(n2)
                    l2 += 1
            return ans
        
        def merge_sort(num):
            if len(num) == 1:
                return num
            mid = len(num) // 2
            left = merge_sort(num[:mid])
            right = merge_sort(num[mid:])
            return merge(left, right)
        
        merge_sort(dif)
        return self.count