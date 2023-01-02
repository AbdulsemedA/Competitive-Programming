class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        Lists = []
        diction = {}
        
        for item in cpdomains:
            Lists.append(item.split(" "))
            Lists[-1][0] = int(Lists[-1][0])
            Lists[-1][1] = Lists[-1][1].split(".")
            
        size = len(Lists)
        
        for item in range(size):
            while len(Lists[item][1]) > 0:
                diction['.'.join(Lists[item][1])] = Lists[item][0] + diction.get('.'.join(Lists[item][1]),0)
                Lists[item][1].pop(0)
                
        return [str(f'{val} {key}') for key,val in diction.items()]
        
        