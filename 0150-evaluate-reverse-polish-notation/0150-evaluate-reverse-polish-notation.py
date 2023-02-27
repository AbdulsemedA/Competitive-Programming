class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a+b)
                
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
                
            elif i == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a*b)
                
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                val = b / a
                val = ceil(val) if val < 0 else floor(val)
                stack.append(val)
                
            else:
                stack.append(int(i))
            
        return stack[-1]
        