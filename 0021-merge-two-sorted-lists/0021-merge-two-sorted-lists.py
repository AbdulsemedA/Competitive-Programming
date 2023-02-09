# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = new = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                tmp.next = list1
                tmp = tmp.next
                list1 = list1.next
            else:
                tmp.next = list2
                tmp = tmp.next
                list2 = list2.next
                
        while list1:
            tmp.next = list1
            tmp = tmp.next
            list1 = list1.next
            
        while list2:
            tmp.next = list2
            tmp = tmp.next
            list2 = list2.next
        
        return new.next
            
            
                
        