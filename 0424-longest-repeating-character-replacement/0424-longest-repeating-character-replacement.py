class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        count = {}
        max_count = 0
        max_len = 0

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            if right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len

            
        