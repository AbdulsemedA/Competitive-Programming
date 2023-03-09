class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        st = [[idx,i[0]] for idx, i in enumerate(intervals)]
        size = len(st)
        end = [i[1] for i in intervals]
        st.sort(key = lambda x: x[1])
        # print(end)
        N = st[-1][1]

        for i in range(size):
            if size == 1 or end[i] > N:
                end[i] = -1
            else:
                l = 0
                r = size - 1

                while l <= r:
                    mid = l + (r - l) // 2
                    if end[i] <= st[mid][1]:
                        r = mid - 1
                    else:
                        l = mid + 1
                end[i] = st[l][0]
        
        return end