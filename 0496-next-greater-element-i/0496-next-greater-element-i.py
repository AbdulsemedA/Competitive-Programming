class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)
        result = []
        greater = [-1] * m
        stack = []
        greats_dict = {}
        
        for idx, num in enumerate(nums2):
            while stack and stack[-1][1] < num:
                j, tmp = stack.pop()
                greater[j] = num
                
            stack.append([idx,num])
        
        for i in range(m):
            greats_dict[nums2[i]] = greater[i]
        
        for i in range(n):
            result.append(greats_dict[nums1[i]])
        
        return result
                
        