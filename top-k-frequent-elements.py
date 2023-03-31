class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Counter = {}
        
        def quick(arr, left, right):
            if not arr:
                return []
            elif left == right:
                Counter[arr[left]] = 1 + Counter.get(arr[left], 0)
                return [arr[left]]
            else:
                pivot = left + (right - left) // 2
                Counter[arr[pivot]] = 1 + Counter.get(arr[pivot], 0)
                first = []
                second = []

                for i in range(len(arr)):
                    if i != pivot:
                        if arr[i] <= arr[pivot]:
                            first.append(arr[i])
                        else:
                            second.append(arr[i])
                
                Left = quick(first, 0, len(first) - 1)
                Right = quick(second, 0, len(second) - 1)

                return Left + [arr[pivot]] + Right
        
        quick(nums, 0, len(nums) - 1)
        # print(Counter)
        elements = [(k, v) for k, v in Counter.items()]
        elements.sort(key = lambda x: x[1], reverse = True)
        ele, val = zip(*elements)
        return ele[:k]