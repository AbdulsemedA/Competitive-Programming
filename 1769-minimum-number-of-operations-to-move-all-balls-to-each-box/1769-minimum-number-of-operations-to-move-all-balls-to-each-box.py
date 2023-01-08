class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        mylist = [val for val in boxes]
        size = len(mylist)
        answer = [0] * size
        
        for index in range(size):
            for index2 in range(size):
                if mylist[index2] == "1":
                    answer[index] += abs(index2 - index)
            
        return answer
        