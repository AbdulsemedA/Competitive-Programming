class Node:    
    def __init__(self, val = None):      
        self.val = val        
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.n = 0
        
    def get(self, index: int) -> int:
        if index < 0 and index >= self.n:
            return -1
        counter = 0
        curr = self.head
        while curr:
            if counter == index:
                return curr.val
            counter += 1
            curr = curr.next
        
        return -1
    
    def addAtHead(self, val: int) -> None:
        beg = Node(val)
        beg.next = self.head
        self.head = beg
        self.n += 1
        

    def addAtTail(self, val: int) -> None:
        tail = Node(val)
        curr = self.head
        if self.n > 0:
            while curr and curr.next:
                curr = curr.next

            curr.next = tail
        else:
            self.head = tail
        self.n += 1
    
    def addAtIndex(self, index: int, val: int) -> None:    
        new = Node(val)
        if index < 0 and index > self.n:
            return
        if index == 0:
            new.next = self.head
            self.head = new
            self.n += 1
        else:
            counter = 0
            dummy = self.head

            while self.head:
                if counter == index - 1:
                    temp = self.head.next
                    self.head.next = new
                    new.next = temp
                    self.n += 1
                    break
                counter += 1
                self.head = self.head.next
            self.head = dummy
                
            if counter == index:
                self.addAtTail(val)
                self.n += 1
            
        
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 and index >= self.n:
            return -1
        
        if index == 0:
            self.head = self.head.next
            self.n -= 1
        else:
            counter = 0
            dummy = self.head
            
            while self.head and self.head.next:
                if counter == index-1:
                    temp = self.head.next
                    if temp.next is None:
                        self.head.next = None
                    else:
                        self.head.next = temp.next
                    self.n -= 1
                    break
                counter += 1
                self.head = self.head.next
            
            self.head = dummy
            # self.n -= 1
                
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)