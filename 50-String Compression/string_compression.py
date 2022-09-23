class Solution:
    def compress(self, chars: List[str]) -> List[int]:
        s = ""
        counter = 0
        current = chars[0]
        for i in chars:
            if i == current:
                counter+=1
            else:
                if counter > 1:
                    s+= current + str(counter)
                else:
                    s+= current
                current = i
                counter = 1
        if counter > 1:
            s+= current + str(counter)
        else:
            s+= current
        chars.clear()
        for i in s:
            chars.append(i)
        return len(chars)
