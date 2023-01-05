class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        total = "'".join(source)
        answer = [""]
        total += "'"
        size = len(total)
        index = 0
        end = 0
        if size > 2:
            while index < size-1:
                if total[index] == "/" and total[index+1] == "/":
                    index += 2
                    while total[index] != "'":
                        index += 1
                elif total[index] == "/" and total[index+1] == "*":
                    index += 2
                    while total[index:index+2] != "*/":
                        index += 1
                    index += 2
                elif total[index] == "'":
                    answer.append("")
                    index += 1
                else:
                    answer[-1] += total[index]
                    index += 1
    
        return [ans for ans in answer if ans != ""]
    
    
     # "a/*com/*ment'l/*ine'm*/or/*e_com/*me*/nt*/b"
     # "a//*b//*c","blank","d//*e/*/f"