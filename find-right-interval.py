class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        st = [intervals[i][0] for i in range(len(intervals))]
        end = [intervals[i][1] for i in range(len(intervals))]
        N = max(st)
        size = len(st)
        start = sorted(st)

        for i in range(size):
            if size == 1:
                end[i] = -1
                break
            if end[i] > N:
                end[i] = -1
            else:
                left = 0
                right = size - 1

                while left <= right:
                    mid = left + (right - left) // 2
                    if end[i] <= start[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                end[i] = st.index(start[left])
        
        return end