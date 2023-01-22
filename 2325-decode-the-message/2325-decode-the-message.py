class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        i = 97
        Kmap = {' ':' '}

        for item in key:
            if item not in Kmap:
                if item != ' ':
                    Kmap[item] = chr(i)
                    i += 1
                else:
                    Kmap[item] = item
        
        return ''.join([Kmap[item] for item in message])
        
        