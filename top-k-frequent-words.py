class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        arr = list(freq.items())
        self.k = k
        
        return [i[0] for i in self.HeapSort(arr, len(arr))][::-1]
        
    def heapify(self,arr,n,i):
        lrg = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n:
            if arr[i][1] < arr[l][1]:
                lrg = l
            elif arr[i][1] == arr[l][1]:
                if arr[i][0] > arr[l][0]:
                    lrg = l

        if r < n:
            if arr[lrg][1] < arr[r][1]:
                lrg = r
            elif arr[lrg][1] == arr[r][1]:
                if arr[lrg][0] > arr[r][0]:
                    lrg = r

        if lrg != i:
            arr[i], arr[lrg] = arr[lrg], arr[i]

            self.heapify(arr, n, lrg)

    def buildHeap(self,arr,n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        for i in range(n - 1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

        return arr[n - self.k:]