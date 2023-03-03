class Solution:
    def balancedString(self, s: str) -> int:
        # number of times each char should occur
        limit = len(s) // 4
        # count the frequency of the chars
        Tc = Counter(s)
        # collect the chars with frequencies above limit
        flip = {i: Tc[i] - limit for i in Tc if Tc[i] > limit}
        Sub = {}
        left = right = 0
        n = len(s)
        required = len(flip)
        created = 0
        L, R = 0, n

        if not flip:
            return 0
         
        # loop for finding the minimum length of the substring when flipped will
        # result in a balanced string

        while right < n:
            curr = s[right]
            Sub[curr] = Sub.get(curr, 0) + 1
            
            # counting the chars found in the flip count
            if curr in flip and Sub[curr] == flip[curr]:
                created += 1
                
            # minimizing the window as much as possible while the two substrings
            # are equal
            while created == required and left <= right:
                if right - left + 1 < R - L + 1:
                    L, R = left, right
                    
                before = s[left]
                Sub[before] -= 1
                
                # shrinking the window from the left side
                if before in flip and Sub[before] < flip[before]:
                    created -= 1
                
                left += 1

            right += 1

        return R - L + 1