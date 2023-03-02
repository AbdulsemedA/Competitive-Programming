class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        result = []

        for i in stack:
            if i == "." or i == "":
                continue
            elif i == "..":
                if result:
                    result.pop()
            else:
                result.append(i)

        return '/' + '/'.join(result)
            




















n = 0

        # for i in path:
        #     if i == ".":
        #         dir_count = 0
        #         if n >= 2:
        #             if stack[-1] == "." and stack[-2] == "/":
        #                 while n > 0 and dir_count < 2:
        #                     if stack[-1] == "/":
        #                         dir_count += 1
        #                     print(stack[-1])
        #                     stack.pop()
        #                     n -= 1
        #                     # print(*stack)
        #                 stack.append("/")
        #                 n += 1
        #             else:
        #                 stack.append(i)
        #                 n += 1
        #         elif n >= 1:
        #             if stack[-1] == "/":
        #                 stack.pop()
        #                 n -= 1
        #             stack.append("/")
        #             n += 1
        #         else:
        #             stack.append(i)
        #             n += 1
                    
        #     elif i == "/":
        #         dir_count = 0
        #         if n >= 3:
        #             if stack[-1] == stack[-2] == "." and stack[-3] != ".":
        #                 while n > 0 and dir_count < 2:
        #                     if stack[-1] == "/":
        #                         dir_count += 1
        #                     print(stack[-1])
        #                     stack.pop()
        #                     n -= 1
        #                     # print(*stack)
        #                 stack.append("/")
        #                 n += 1
        #             else:
        #                 if stack[-1] != "/":
        #                     if n >= 2 and stack[-1] == "." and stack[-2] == "/":
        #                         stack.pop()
        #                         n -= 1
        #                     else:
        #                         stack.append(i)
        #                         n += 1


        #         elif not stack or stack[-1] != "/":
        #             if n >= 2 and stack[-1] == "." and stack[-2] == "/":
        #                 stack.pop()
        #                 n -= 1
        #             else:
        #                 stack.append(i)
        #                 n += 1
        #     else:
        #         stack.append(i)
        #         n += 1