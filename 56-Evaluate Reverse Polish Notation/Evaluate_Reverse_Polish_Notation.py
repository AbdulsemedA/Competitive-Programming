class Solution:
    def IsNumericDigit(self, C: str) -> bool: 
        if C >= '-200' and C <= '200':
            return True
        return False
    
    def IsOperator(self, C: str) -> bool:
        if C == '+' or C == '-' or C == '*' or C == '/':
            return True
        return False

    def PerformOperation(self, operation: chr, operand1: int, operand2: int) -> int:
        if operation == '+':
            return operand1 + operand2
        elif operation == '-': 
            return operand1 - operand2
        elif operation == '*': 
            return operand1 * operand2
        elif operation == '/':
            return int(operand1 / operand2)
        else: 
            return -1
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            op_check = self.IsOperator(i) 
            dig_check = self.IsNumericDigit(i)
            if op_check:
                operand2,operand1 = stack.pop(),stack.pop()
                result = self.PerformOperation(i, operand1, operand2); 
                stack.append(result)
            elif int(i) in range(-200,200):
                stack.append(int(i))
        return stack[-1]
