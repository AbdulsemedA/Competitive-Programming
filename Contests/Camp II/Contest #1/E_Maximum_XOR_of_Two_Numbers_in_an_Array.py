# class TrieNode:
#     def __init__(self):
#         self.child = {}

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, n):
#         temp = self.root
#         i = 31

#         while i >= 0:
#             bit = (n >> i) & 1

#             if bit not in temp.child:
#                 temp.child[bit] = TrieNode()

#             temp = temp.child[bit]
#             i -= 1

#     def max_xor_helper(self, value):
#         temp = self.root
#         curr = 0
#         i = 31
#         while i >= 0:
#             bit = (value >> i) & 1
#             if bit ^ 1 in temp.child:
#                 temp = temp.child[bit ^ 1]
#                 curr += (1 << i)
#             else:
#                 temp = temp.child[bit]

#             i -= 1
#         return curr

# class Solution:
#     def solve(self, A):
#         trie = Trie()
#         max_val = 0
#         trie.insert(A[0])
#         for n in A[1:]:
#             max_val = max(trie.max_xor_helper(n), max_val)
#             trie.insert(n)
#         return max_val

# testcase = int(input())

# for _ in range(testcase):
#     n = int(input())
#     A = list(map(int, input().split()))
#     ob = Solution()
#     print(ob.solve(A))

from typing import List


class TrieNode:
    def __init__(self):
        self.kids = [None]*2
        self.isEnd = False
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, bite):
        cur = self.root
        
        for bit in bite:
            bit = int(bit)
            if cur.kids[bit] == None:
                cur.kids[bit] = TrieNode()
                
            cur = cur.kids[bit]
          
        cur.isEnd = True
        
    def max_val(self, bite):
        cur = self.root
        res = ""
        
        for bit in bite:
            bit = int(bit)
            if bit == 0:
                if cur.kids[1] != None:
                    cur = cur.kids[1]
                    res += '1'
                else:
                    cur = cur.kids[0]
                    res += '0' 
            else:
                if cur.kids[0] != None:
                    cur = cur.kids[0]
                    res += '0'
                else:
                    cur = cur.kids[1]
                    res += '1'
        return res
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            bin_val = bin(num)[2:]
            bit_rep = "0" * (32 - len(bin_val)) + bin_val
            trie.insert(bit_rep)
            
        max_val = 0
        for num in nums:
            bin_val = bin(5)[2:] 
            bit_rep = "0" * (32 - len(bin_val)) + bin_val
            ans = int(trie.max_val(bit_rep), 2)
            # print(ans)
            max_val = max(max_val, ans ^ num)
            
        return max_val

obj = Solution()

tc = int(input())

for _ in range(tc):
    n = int(input())
    num = list(map(int, input().split()))
    print(obj.findMaximumXOR(num))