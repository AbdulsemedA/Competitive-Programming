class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        result_string = []
        if n > 1:
            right = 1
            current = chars[0]
            freq = 1
        
            while right < n:
                if chars[right] == current:
                    freq += 1
                else:
                    result_string.append(current)
                    if freq > 1:
                        result_string.extend([x for x in str(freq)])
                        freq = 1
                    current = chars[right]
                right += 1
            
            result_string.append(chars[right-1])
            
            if freq > 1:
                result_string.extend([x for x in str(freq)])
                
            chars.clear()
            chars.extend(result_string)
            
            return len(chars)
        else:
            return len(chars)
            
        
        