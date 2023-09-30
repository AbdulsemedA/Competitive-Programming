class TrieNode:
    def __init__(self, val):
        self.children = [None for _ in range(26)]
        self.val = val

class MapSum:
    def __init__(self):
        self.root = TrieNode(0) 
        self.Hmap = {}       

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        sub = 0
        
        if key in self.Hmap:
            sub = self.Hmap[key]
        self.Hmap[key] = val

        for wrd in key:
            char = ord(wrd) - ord('a')

            if curr.children[char] is None:
                curr.children[char] = TrieNode(val)
            else:
                curr.children[char].val += val - sub
                
            curr = curr.children[char]        

    def sum(self, prefix: str) -> int:
        curr = self.root

        for wrd in prefix:
            char = ord(wrd) - ord('a')

            if curr.children[char] is None:
                return 0    
            curr = curr.children[char]
        
        return curr.val
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)