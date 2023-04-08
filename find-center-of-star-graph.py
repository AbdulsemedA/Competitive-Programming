class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        unique = set()
        for i in edges:
            src, des = i
            if src in unique: return src
            if des in unique: return des
            unique.add(src)
            unique.add(des)