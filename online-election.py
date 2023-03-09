class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leader = []
        freq = {}

        for i in persons:
            freq[i] = 1 + freq.get(i,0)
            if not self.leader or freq[i] >= self.leader[-1][1]:
                self.leader.append([i, freq[i]])
            else:
                self.leader.append(self.leader[-1])
        
    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if self.times[mid] > t:
                right = mid - 1
            else:
                left = mid + 1
        
        print("leader: ",self.leader[left-1][0])

        return self.leader[left-1][0]
        
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)