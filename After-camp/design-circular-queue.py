class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.k = k
        self.front = self.rear = -1
        

    def enQueue(self, value: int) -> bool:
        if self.front == 0 and self.rear == self.k - 1:
            return
        if self.front == self.rear + 1:
            return
        
        if self.front == -1:
            self.front = self.rear = 0
        else:
            if self.rear == self.k - 1:
                self.rear = 0
            else:
                self.rear += 1
        
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.front == -1: return
        
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            if self.front == self.k - 1:
                self.front = 0
            else:
                self.front += 1
        
        return True

    def Front(self) -> int:
        return self.queue[self.front] if self.front > -1 else -1
        
    def Rear(self) -> int:
        return self.queue[self.rear] if self.rear > -1 else -1
        
    def isEmpty(self) -> bool:
        return self.front == self.rear == -1

    def isFull(self) -> bool:
        if self.front == 0 and self.rear == self.k-1:
            return True
        if self.front == self.rear + 1:
            return True

        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()