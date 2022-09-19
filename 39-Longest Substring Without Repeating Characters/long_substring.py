class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        for i in s:
            chars.append(i)
        maxi = 0
        counter = []
        for i in range(len(chars)):
            counter.append(chars[i])
            for j in range(i+1,len(chars)):
                if chars[j] not in counter:
                    counter.append(chars[j])
                else:
                    break
            if int(len(counter)) >= maxi:
                maxi = len(counter)
            counter.clear()
        return maxi
                    
