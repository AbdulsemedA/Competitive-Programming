class Solution:
    def reverseString(self, s: List[str], left = 0, right = 0) -> None:
        if right == 0:
            if len(s) > 1:
                self.reverseString(s,left,len(s)-1)
            return
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        self.reverseString(s,left+1,right-1)