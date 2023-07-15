class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = [(nums1[0] + nums2[0], 0, 0)]
        pairs = []

        while queue and len(pairs) < k:
            val, u, v = heapq.heappop(queue)
            pairs.append([nums1[u], nums2[v]])
            
            if v == 0 and u + 1 < len(nums1):
                heapq.heappush(queue, (nums1[u+1] + nums2[v], u + 1, v))
            if v + 1 < len(nums2):
                heapq.heappush(queue, (nums1[u] + nums2[v+1], u, v + 1))

        return pairs