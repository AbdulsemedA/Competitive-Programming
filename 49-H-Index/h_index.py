class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        indexes = []
        for j in range(max(citations)+1):
            counter = 0
            for i in citations:
                if i >= j:
                    counter+=1
            if counter >= j:
                indexes.append(j)
        return max(indexes)
