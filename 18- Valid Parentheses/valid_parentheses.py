class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        arr2 = []
        for i in s:
            arr.append(i)
        for j in range(len(arr)):
            if arr[j] in ["(","[","{"]:
                arr2.append(arr[j])
            elif arr[j] in [")","]","}"]:
                if arr[j] == ")":
                    if j!=0 and len(arr2) > 0:
                        if arr2[len(arr2)-1] == "(":
                            arr2.pop()
                        else:
                            return False
                    else:
                            return False
                elif arr[j] == "]":
                    if j!=0 and len(arr2) > 0:
                        if arr2[len(arr2)-1] == "[":
                            arr2.pop()
                        else:
                            return False
                    else:
                            return False
                elif arr[j] == "}":
                    if j!=0 and len(arr2) > 0:
                        if arr2[len(arr2)-1] == "{":
                            arr2.pop()
                        else:
                            return False
                    else:
                        return False
        if len(arr2) == 0:
            return True
        else:
            return False
