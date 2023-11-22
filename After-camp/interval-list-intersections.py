class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        fst = snd = 0
        res = []

        while fst < len(firstList) and snd < len(secondList):
            start = max(firstList[fst][0], secondList[snd][0])
            end = min(firstList[fst][1], secondList[snd][1])

            if end - start > -1:
                res.append([start, end])

            if firstList[fst][1] < secondList[snd][1]:
                fst += 1
            else:
                snd += 1

        return res
        