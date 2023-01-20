class Solution: 
    def select(self, arr, i):
        return i
    
    def selectionSort(self, array,n):
        for i in range(n):
            min_idx = self.select(array,i)
            for j in range(i + 1, n):
                if array[min_idx] > array[j]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
            
        return array
        
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
