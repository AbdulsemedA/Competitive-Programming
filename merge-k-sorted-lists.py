# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        matrix = []
        heap = []
        total = 0
        ans = []

        for ele in lists:
            matrix.append([])
            while ele:
                matrix[-1].append(ele.val)
                total += 1
                ele = ele.next
        
        for i in range(len(matrix)):
            if matrix[i]:
                heapq.heappush(heap, (matrix[i][0], i, 0))
        
        for i in range(total):
            val, row, col = heapq.heappop(heap)
            ans.append(val)
            if col < len(matrix[row]) - 1:
                heapq.heappush(heap, (matrix[row][col+1], row, col+1))
        
        ans.sort(reverse=True)
        head = None

        for i in ans:
            head = ListNode(i,next=head)
        return head