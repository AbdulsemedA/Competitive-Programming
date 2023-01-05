class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        A = m - 1      # The last index of nums1
        B = A + n      # The last index of the open space for nums2 filled with 0's
        C = n - 1      # The last index of nums2
        
        while C > -1 and A > -1 and B > -1:
            if nums2[C] >= nums1[A]:
                nums1[B] = nums2[C]
                B -= 1
                C -= 1
            else:
                nums1[B] = nums1[A]
                B -= 1
                A -= 1
                
        if C > -1:
            while C > -1:
                nums1[B] = nums2[C]
                C -= 1
                B -= 1
        
                
        