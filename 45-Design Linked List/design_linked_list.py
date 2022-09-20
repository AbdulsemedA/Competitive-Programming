class MyLinkedList:

    def __init__(self):
        self.arr = []
        
    def get(self, index: int) -> int:
        if index < len(self.arr):
            return self.arr[index]
        return -1
        
    def addAtHead(self, val: int) -> None:
        self.arr.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.arr.append(val)
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= len(self.arr):
            self.arr.insert(index,val)
        return
        
    def deleteAtIndex(self, index: int) -> None:
        if len(self.arr) > index:
            self.arr.pop(index)
        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
