class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        v4 = queryIP.split('.')
        v6 = queryIP.split(':')
        
        if len(v4) != 4 and len(v6) != 8:
            return 'Neither'
        
        if len(v4) == 4 and len(v6) != 8:
            for i in range(len(v4)):
                if v4[i].isnumeric() and 0 <= int(v4[i]) <= 255:
                    if len(str(int(v4[i]))) == len(v4[i]):
                        continue
                return 'Neither'
            return 'IPv4'

        elif len(v4) != 4 and len(v6) == 8:
            for ele in v6:
                if 1 <= len(ele) <= 4:
                    for ch in ele:
                        if 48 <= ord(ch) <= 57 or 97 <= ord(ch) <= 102 or 65 <= ord(ch) <= 70:
                            continue
                        return 'Neither'
                else:
                    return 'Neither'
            return 'IPv6'