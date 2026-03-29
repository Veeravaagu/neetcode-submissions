class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] < num:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1*num)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heapop(self.large)
            heapq.heappush(self.small, -1*val)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-1 * self.small[0] + self.large[0]) / 2.0
        if len(self.small) > len(self.large):
            return (-1 * self.small[0])
        return self.large[0]
        