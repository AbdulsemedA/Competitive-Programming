class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                score = stack.pop()                
                if score == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * score
                
        return stack[-1]
            
                
                
        