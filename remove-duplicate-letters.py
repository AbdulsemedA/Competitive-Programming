class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        n = len(s)
        unique = set()
        last_occur = {}

        for i in range(n):
            last_occur[s[i]] = i

        for i in range(n):
            if s[i] not in unique:
                while stack and stack[-1] > s[i] and i < last_occur[stack[-1]]:
                    unique.remove(stack.pop())
                unique.add(s[i])
                stack.append(s[i])

        return ''.join(stack)