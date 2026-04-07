class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            val1 = heapq.heappop(maxHeap)
            val2 = heapq.heappop(maxHeap)

            if val1 != val2:
                heapq.heappush(maxHeap, val1 - val2)
        return maxHeap[0] * -1 if len(maxHeap) == 1 else 0
        