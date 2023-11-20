class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    
        for ele in asteroids:
            while stack and ele < 0 < stack[-1] and stack[-1] < -ele:
                stack.pop()
            
            if not stack or ele > 0 or stack[-1] < 0:
                stack.append(ele)
                
            elif ele < 0 and stack[-1] == -ele:
                stack.pop()
        
        return stack