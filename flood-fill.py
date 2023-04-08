class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        if image[sr][sc] == color:
            return image
        
        if sr < 0 or sr >= n or sc < 0 or sc >= m:
            return image

        stack = [(sr, sc)]
        ocol = image[sr][sc]
        while stack:
            x, y = stack.pop()
            if image[x][y] == ocol:
                image[x][y] = color
                if x > 0:
                    stack.append((x-1, y))
                if x < n-1:
                    stack.append((x+1, y))
                if y > 0:
                    stack.append((x, y-1))
                if y < m-1:
                    stack.append((x, y+1))

        return image