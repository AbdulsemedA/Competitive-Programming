class Solution:
    def findComplement(self, num: int) -> int:
        bnr = bin(num)[2:]
        converted = [str(1 - int(i)) for i in bnr if i.isnumeric()] 
        return int("".join(converted), 2)