class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Solved Myself in under 15 mins but had to get help from GPT with some tuple and math syntax
        output = []
        for i in range(len(points)):
            points[i] = (math.sqrt(pow(points[i][0], 2) + pow(points[i][1], 2)), [points[i][0], points[i][1]])
        heapq.heapify(points)
        while k > 0:
            res = heapq.heappop(points)
            output.append(res[1])
            k -= 1
        return output
        