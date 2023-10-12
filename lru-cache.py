class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.caches = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def add_to_front(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def move_to_front(self, node):
        self.remove_node(node)
        self.add_to_front(node)

    def remove_least(self):
        least_node = self.tail.prev
        del self.caches[least_node.key]
        self.remove_node(least_node)
    
    def get(self, key: int) -> int:
        if key in self.caches:
            node = self.caches[key]
            self.move_to_front(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.caches:
            node = self.caches[key]
            node.value = value
            self.move_to_front(node)
        else:
            if len(self.caches) == self.capacity:
                self.remove_least()
            new_node = ListNode(key, value)
            self.caches[key] = new_node
            self.add_to_front(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)