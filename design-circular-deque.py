class MyCircularDeque:

    def __init__(self, k: int):
        self.front = -1
        self.rear = 0
        self.size = k
        self.items = 0
        self.deque = [None] * k
        
        
    def insertFirst(self,value:int)->bool:
        self.front = self.rear = 0
        self.deque[self.front] = value
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.front == -1:
            self.insertFirst(value)
            return True
        
        if self.front == 0:
            self.front = self.size -1
        else:
            self.front -= 1
        self.deque[self.front] = value
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.front == -1:
            self.insertFirst(value)
            return True
        if self.rear == self.size-1:
            self.rear = 0
        else:
            self.rear += 1
        self.deque[self.rear] = value

        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
            return True
        
        if self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
            return True
        if self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1
        return True
        
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]
        
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        if self.front == -1:
            return True
        return False
        

    def isFull(self) -> bool:
        if (self.front == 0) and (self.rear == self.size-1):
            return True
        elif (self.front == self.rear+1):
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()