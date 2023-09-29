class TrieNode:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.count = 1
        self.end = False
   
class Solution:
    def __init__(self):
        self.root = TrieNode() 
        
    def insert(self, word: str) -> None:
        curr = self.root
        
        for wrd in word:
            char = ord(wrd) - ord('a')

            if curr.child[char] is None:
                curr.child[char] = TrieNode()
            else:
                curr.count += 1
                
            curr = curr.child[char]
        curr.end = True

    def valid(self, word: str) -> bool:
        curr = self.root
        
        for idx in range(len(word)):
            char = ord(word[idx]) - ord('a')

            if curr.child[char] is None:
                return False
            
            if idx < len(word) - 1 and curr.count == 1:
                return False
            
            if not curr.child[char].end:
                return False
            
            curr = curr.child[char]
            
        return True

    def longestWord(self, words: List[str]) -> str:
        ans, size = '', 0

        for word in words:
            self.insert(word)

        for word in words:
            if self.valid(word):
                if len(word) > size:
                    ans = word
                    size = len(word)
                elif len(word) == size:
                    if ans > word:
                        ans = word
        
        return ans