class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [None] * len(parent)
        self.children = [[] for _ in range(len(parent))]

        for i, p in enumerate(parent):
            if p != -1: self.children[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        if not self.locked[num]:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = None
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num]: return False
        
        locked_descendants = False
        node = num

        while self.parent[node] != -1:
            node = self.parent[node]

            if self.locked[node]: return False

        def dfs(node):
            nonlocal locked_descendants

            if self.locked[node]:
                locked_descendants = True
                self.locked[node] = None

            for child in self.children[node]:
                dfs(child)

        dfs(num)

        if not locked_descendants: return False

        self.locked[num] = user
        return True
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)