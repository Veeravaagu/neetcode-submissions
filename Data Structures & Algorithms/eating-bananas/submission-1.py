class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        temp = 0
        while low <= high:
            mid = (low + high) // 2
            k = 0
            for n in piles:
                k += math.ceil(n / mid)
            if k > h:
                low = mid + 1
            elif k <= h:
                high = mid - 1
                temp = mid
        return temp