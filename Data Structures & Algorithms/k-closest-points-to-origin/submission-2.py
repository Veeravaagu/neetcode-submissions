class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for i in range(len(points)):
            dist = (math.sqrt((points[i][0] - 0)**2 + (points[i][1] - 0)**2))
            heap.append((dist, points[i]))
        heapq.heapify(heap)
        while k > 0:
            k -= 1
            euc_dist, point = (heapq.heappop(heap))
            res.append(point)
        return res
        