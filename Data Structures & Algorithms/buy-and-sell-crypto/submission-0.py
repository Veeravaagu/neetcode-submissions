class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        profit = 0
        while L < R and R < len(prices):
            if prices[L] <= prices[R]:
                profit = max(profit, prices[R] - prices[L])
                R += 1
            else:
                L = R
                R += 1
        return profit
        