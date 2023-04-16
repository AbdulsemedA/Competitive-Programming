class ThroneInheritance:

    def __init__(self, kingName: str):
        self.family = defaultdict(list)
        self.family[kingName] = []
        self.dead = set()
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []

        def dfs(node):
            nonlocal order
            if node not in self.dead: 
                order.append(node)
            
            if self.family[node]:
                for ele in self.family[node]:
                    dfs(ele)

        dfs(self.kingName)
        return order
        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()