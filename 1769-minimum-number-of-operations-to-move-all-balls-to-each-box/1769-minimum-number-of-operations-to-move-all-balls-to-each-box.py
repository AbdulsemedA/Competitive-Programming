class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        mylist = [val for val in boxes]
        size = len(mylist)
        answer = [0] * size
        for index in range(size):
            current = 0
            for index2 in range(size):
                if mylist[index2] == "1":
                    current += abs(index2 - index)
            answer[index] = current
        
        return answer
        