class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in range(len(word)):
            char = ord(word[i]) - ord('a')

            if curr.children[char] is None:
                curr.children[char] = TrieNode()
                
            curr = curr.children[char]
        
        curr.is_end = True

    def regexp(self, root, word):
        curr = root

        for wrd in range(len(word)):
            if word[wrd] == '.':
                for i in range(26):
                    if curr.children[i]:
                        if self.regexp(curr.children[i], word[wrd+1:]):
                            return True
                return False
            else:
                char = ord(word[wrd]) - ord('a')

                if curr.children[char] is None:
                    return False    
                curr = curr.children[char]
        
        return curr.is_end == True

    def search(self, word: str) -> bool:
        curr = self.root

        for wrd in range(len(word)):
            if word[wrd] == '.':
                for i in range(26):
                    if curr.children[i]:
                        if self.regexp(curr.children[i], word[wrd+1:]):
                            return True
                return False
            
            else:
                char = ord(word[wrd]) - ord('a')

                if curr.children[char] is None:
                    return False    
                curr = curr.children[char]
        
        return curr.is_end == True
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)