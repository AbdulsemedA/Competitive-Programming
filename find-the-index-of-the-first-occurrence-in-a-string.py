class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            window = str(haystack[i:i+len(needle)])
            
            if window == needle:
                return i
        
        return -1