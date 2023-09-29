class TrieNode:
    def __init__(self, val):
        self.is_end = False
        self.child = [None]
        self.val = val

class Solution:
    def __init__(self):
        self.root = TrieNode('')

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        curr = self.root
        exist = defaultdict(str)

        for wrd in s:
            if curr.child[0] is None:
                curr.child[0] = TrieNode(wrd)
                
            curr = curr.child[0]
        
        curr.is_end = True

        def isSubseq(word):
            n = len(word)
            l = 0
            curr = self.root
            
            while l < n and curr:
                if curr and curr.child[0] and curr.child[0].val == word[l]:
                    l += 1

                curr = curr.child[0]
            
            return l == n
        
        ans = 0

        for wrd in words:
            if wrd in exist:
                if exist[wrd]:
                    ans += 1
            else:
                if isSubseq(wrd):
                    exist[wrd] = True
                    ans += 1
                else:
                    exist[wrd] = False
        
        return ans