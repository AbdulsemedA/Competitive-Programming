class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        arr.sort(key=lambda test_string : list(
        map(int, re.findall(r'\d+', test_string)))[0])
        aaa = []
        for item in arr:
            aaa.append(item[:-1])
        result = ' '.join(aaa)
        return result
