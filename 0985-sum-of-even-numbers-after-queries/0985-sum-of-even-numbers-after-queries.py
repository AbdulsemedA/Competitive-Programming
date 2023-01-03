class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = sum([i for i in nums if abs(i) % 2 == 0])
        answer = [even]
        
        for item in queries:
            temp = nums[item[1]]
            nums[item[1]] += item[0]
            if abs(nums[item[1]]) % 2 != 0:
                if abs(temp) % 2 == 0:
                    answer.append(answer[-1] - temp)
                else:
                    answer.append(answer[-1])
            else:
                change = answer[-1] + nums[item[1]]
                if abs(temp) % 2 == 0:
                    change -= temp
                answer.append(change)
            
        return answer[1:]
        