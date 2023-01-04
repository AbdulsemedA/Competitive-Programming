import collections
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        myList = []
        for item in paths:
            myList.append(list(item.split(" ")))
        
        all_path = []
        for item in range(len(myList)):
            for element in range(1,len(myList[item])):
                all_path.append(str(myList[item][0] + " " + myList[item][element]))
        
        for index in range(len(all_path)):
            all_path[index] = list(all_path[index].split("("))
            all_path[index][0] = all_path[index][0].replace(" ","/")
            all_path[index][-1] = all_path[index][-1][:-1]
        
        diction = defaultdict(list)
        
        for index in range(len(all_path)):
            diction[all_path[index][1]].append(index)
        
        answer = []
        
        for item in diction:
            current = []
            for val in diction[item]:
                if len(diction[item]) > 1:
                    current.append(all_path[val][0])   
            if len(current) > 1:
                answer.append(current)
        
        return answer
            
                
        