class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = {
            (1, 0): [(0, 1), (0, -1)],
            (0, 1): [(-1, 0), (1, 0)],
            (-1, 0): [(0, -1), (0, 1)],
            (0, -1): [(1, 0), (-1, 0)]
        }

        curr = [0, 0]
        face = (0, 1)

        for cmd in instructions:
            if cmd == 'G':
                curr[0] += face[0]
                curr[1] += face[1]
            elif cmd == 'R':
                face = direction[face][1]
            else:
                face = direction[face][0]

        return curr == [0, 0] or face != (0 , 1)