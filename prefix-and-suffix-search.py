class TrieNode:
    def __init__(self):
        self.child = [None for _ in range(27)]
        self.idx = -1
        
class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.words = words
        
        for idx, wrd in enumerate(words):
            self.combination(wrd, idx)
    
    def insert(self, word, idx):
        curr = self.root

        for wrd in word:
            letter = ord(wrd) - 97

            if curr.child[letter] is None:
                curr.child[letter] = TrieNode()
            
            curr.idx = idx
            curr = curr.child[letter]
            
        curr.idx = idx

    def combination(self, word, idx):
        for index in range(len(word) + 1):
            letter = word[index:] + '{' + word
            self.insert(letter, idx)
    
    
    def f(self, pref: str, suff: str) -> int:
        curr = self.root
        letter = suff + '{' + pref
        
        for wrd in letter:
            ltr = ord(wrd) - 97

            if curr.child[ltr] is None:
                return -1
            
            curr = curr.child[ltr]
            
        return curr.idx

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)