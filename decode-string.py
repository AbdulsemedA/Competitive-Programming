class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
    
        for i in s:
            if i == ']':
                letters = []
                while stack and stack[-1] != '[':
                    letters.append(stack.pop())
                stack.pop()
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                new = letters[::-1] * int(''.join(num[::-1]))
                stack.extend(new)
                continue
            stack.append(i)
            
        answer = "".join(stack)

        if answer.isdigit():
            return ""
        return answer
            
        return ''.join(stack)