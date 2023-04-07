class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def all_primes(upper):
            for idx in range(2, upper + 1):
                curr = idx
                
                if is_prime[curr]:
                    while curr <= right:
                        is_prime[curr] = False
                        curr += idx
                    is_prime[idx] = True
                
        is_prime = [True for _ in range(right + 1)]
        is_prime[0] = False
        is_prime[1] = False
        
        upper = ceil(sqrt(right))
        all_primes(upper)
        
        res = []
        for val in range(left, right + 1):
            if is_prime[val]:
                res.append(val)

        diff = [float("inf"), [0, 0]]
        if len(res) > 1:
            for idx in range(1, len(res)):
                diff = min(diff, [(res[idx] - res[idx - 1]), [res[idx - 1], res[idx]]]) 
        else:
            return [-1, -1]
        
        return [diff[1][0], diff[1][1]]