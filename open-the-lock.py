class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        target_num = [int(i) for i in target]
        print(target_num)
        
        visited = set(["0000"])
        queue = deque([[0,0,0,0]])

        def bfs(queue, ans, status):
            while queue:
                size = len(queue)
                ans += 1

                for _ in range(size):
                    curr = queue.popleft()
                    
                    if curr == target_num:
                        status = True
                        break

                    for i in range(4):
                        temp = 0

                        for j in [1, -1]:
                            if j + curr[i] > 9:
                                temp = 0
                            elif curr[i] + j < 0:
                                temp = 9
                            else:
                                temp = curr[i] + j
                            
                            moved = curr[:]
                            moved[i] = temp

                            nextWheel = "".join([str(el) for el in moved])
                            
                            if nextWheel not in visited and nextWheel not in dead:
                                queue.append(moved[:])
                                visited.add(nextWheel)

                if status: break

            return status, ans

        if "0000" in dead:
            return -1

        st, ans = bfs(queue, -1, False)
        return ans if (ans > -1 and st) else -1