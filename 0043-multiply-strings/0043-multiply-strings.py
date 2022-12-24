class Solution:
    def convert_int(self, num: str) -> str:
        result = 0
        
        for i in num:
            """
            ord("0") is used to get the number directly from the string by the
            difference
            """
            result = (result * 10) + (ord(i) - ord("0"))
        
        return result
    
    def multiply(self, num1: str, num2: str) -> str:
        nums1 = self.convert_int(num1)
        nums2 = self.convert_int(num2)
        product = str(nums1 * nums2)
        
        return product
        
        
        
        
        