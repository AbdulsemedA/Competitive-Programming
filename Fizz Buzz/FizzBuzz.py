class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        tmp_result = []
        for i in range(1, n + 1):
            if (i % 3) == 0 and (i % 5) != 0:
                tmp_result.append("Fizz")
            elif (i % 3) == 0 and (i % 5) == 0:
                tmp_result.append("FizzBuzz")
            elif (i % 5) == 0:
                tmp_result.append("Buzz")
            else:
                tmp_result.append(str(i))
        return tmp_result
