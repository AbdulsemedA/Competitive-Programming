class TrieNode:
    def __init__(self):
        self.is_end = False
        self.child = [None for _ in range(26)]
        self.count = 1

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
                curr.child[char].count += 1
                
            curr = curr.child[char]
        curr.end = True
    
    def finder(self, word: str) -> None:
        ans = 0
        curr = self.root

        for wrd in word:
            char = ord(wrd) - ord('a')

            if curr.child[char]:
                ans += curr.child[char].count
            curr = curr.child[char]
        
        return ans

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        answer = []
        for word in words:
            self.insert(word)
        
        for word in words:
            answer.append(self.finder(word))
        
        return answer