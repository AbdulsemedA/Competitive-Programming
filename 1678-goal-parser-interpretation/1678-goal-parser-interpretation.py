class Solution:
    def interpret(self, command: str) -> str:
        comm_stack = []
        
        for char in command:
            if char == ")":
                current = ""
                
                while comm_stack and comm_stack[-1] != "(":
                    current = comm_stack.pop() + current
                    
                comm_stack.pop()
                
                if len(current) == 0:
                    comm_stack.append("o")
                else:
                    comm_stack.append(current)
            else:
                comm_stack.append(char)
                
        return ''.join(comm_stack)
                
                    
        
                                                        
                                            
                
        
        