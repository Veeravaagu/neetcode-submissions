class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Found The Solution but confused over Time Complexity thought it was O(n + nlogm), Also couldn't get the idea to write the syntax for k.
        maxPile = max(piles)
        left = 1
        right = maxPile
        result = right
        while left <= right:
            mid = (left+right)//2
            k = 0
            for p in piles:
                k += math.ceil(float(p)/mid)
            if k <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
        