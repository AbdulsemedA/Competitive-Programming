# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next
        
        def merge_sort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                left = nums[:mid]
                right = nums[mid:]

                merge_sort(left)
                merge_sort(right)

                i = j = k = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        nums[k] = left[i]
                        i += 1
                    else:
                        nums[k] = right[j]
                        j += 1
                    k += 1
                
                while i < len(left):
                    nums[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    nums[k] = right[j]
                    j += 1
                    k += 1
                    
        merge_sort(nums)
        dummy = curr = ListNode(0)
        for i in nums:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next