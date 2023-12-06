class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        x1, y1 = point

        for (x2, y2), n in self.points.items():
            x_diff = abs(x1 - x2)
            y_diff = abs(y1 - y2)

            if x_diff == y_diff and x_diff:
                cr1 = (x1, y2)
                cr2 = (x2, y1)

                if cr1 in self.points and cr2 in self.points:
                    count += n * self.points[cr1] * self.points[cr2]

        return count
        

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)