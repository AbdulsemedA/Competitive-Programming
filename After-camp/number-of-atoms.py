class Solution:
    def countOfAtoms(self, formula: str) -> str:
        atoms = {}
        chem = '(' + formula + ')'
        formula = chem
        n = len(formula)
        curr = 0
        stack = []

        while curr < n:
            if formula[curr] == '(':
                 stack.append('(')
                 curr += 1
                
            elif formula[curr] == ')':
                factor = '1'

                if curr + 1 < n and formula[curr + 1].isdigit():
                    curr += 1
                    factor = ''
                    while curr < n and formula[curr].isdigit():
                        factor += formula[curr]
                        curr += 1
                
                ftr = int(factor)

                arr = []
                unique = set()
                
                while stack and stack[-1] != '(':
                    num = 1
                    
                    if stack[-1].isdigit():
                        num = int(stack.pop())
                        ele = stack.pop()
                        if ele in atoms and ele not in unique:
                            atoms[ele] = 0

                        if ele in atoms:
                            atoms[ele] = ftr * num + atoms.get(ele, 0)
                        else:
                            atoms[ele] = ftr * num
                        arr.append(str(ftr * num))
                        arr.append(ele)
                        unique.add(ele)
                    else:
                        ele = stack.pop()
                        if ele in atoms and ele not in unique:
                            atoms[ele] = 0

                        if ele in atoms:
                            atoms[ele] = atoms.get(ele, 0) + ftr
                        else:
                            atoms[ele] = ftr

                        if atoms[ele]:
                            arr.append(str(ftr))
                        arr.append(ele)
                        unique.add(ele)
                        
                stack.pop()
                stack += arr[::-1]
                
                if ftr == 1:
                    curr += 1
            else:
                digit = ''
                element = ''
                
                if formula[curr].isdigit():
                    
                    while curr < n and formula[curr].isdigit():
                        digit += formula[curr]
                        curr += 1
                    stack.append(digit)
                else:
                    element += formula[curr]
                    curr += 1
                    
                    while curr < n and not formula[curr].isdigit() and formula[curr] != '(' and formula[curr] != ')' and not formula[curr].isupper():
                        element += formula[curr]
                        curr += 1
                    stack.append(element)

        ans = []
        
        for key, value in atoms.items():
            ans.append((key, value))

        ans.sort()
        answer = ''
        
        for k, v in ans:
            answer += k
            if atoms[k] > 1:
                answer += str(v)
        
        return answer


