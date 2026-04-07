class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for i in range(len(points)):
            dist = math.sqrt((points[i][0] ** 2 + points[i][1]**2))
            heapq.heappush(heap, (dist, points[i]))
        while 0 < k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res
        