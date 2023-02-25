class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 1
        for i in range(len(sentences)):
            curr = len(list(map(str, sentences[i].split(" "))))
            maxi = max(maxi, curr)

        return maxi
        