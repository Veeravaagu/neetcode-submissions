class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        L = R = 0
        for R in range (len(prices)):
            profit = max(profit, (prices[R] - prices[L]))
            if prices[L] > prices[R]:
                L = R
        return profit
            
        