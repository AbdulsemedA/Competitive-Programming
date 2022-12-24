class Solution:
    def freqAlphabets(self, s: str) -> str:
        nums_array = [char for char in s]
        strings = ""
         
        while nums_array:
            if nums_array[-1] == "#":
                nums_array.pop()
                num = ""
                
                for i in range(2):
                    num = nums_array.pop() + num
                
                strings = chr(96 + int(num)) + strings
            else:
                strings = chr(96 + int(nums_array.pop())) + strings
        return strings
                    
            
        