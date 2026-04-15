class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            val1 = -heapq.heappop(heap)
            val2 = -heapq.heappop(heap)
            newVal = val1 - val2
            if newVal > 0:
                heapq.heappush(heap, -1 * newVal)
        return heap[0] * -1 if len(heap) == 1 else 0

