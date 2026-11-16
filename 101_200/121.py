class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp, minp = 0, float('inf')
        for i in range(len(prices)):
            if prices[i] < minp:
                minp = prices[i]
            elif prices[i] - minp > maxp:
                maxp = prices[i] - minp
        return maxp
