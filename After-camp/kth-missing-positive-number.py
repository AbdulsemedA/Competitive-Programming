class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        answer = curr = 1
        count = i = 0
        
        while i < len(arr) and count < k:
            if arr[i] == curr:
                i += 1
            else:
                count += 1
            
            answer = curr
            curr += 1

        if count < k:
            answer += k - count
            
        return answer