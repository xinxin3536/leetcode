class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0 
        for i in range(0,len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                maxx = maxx + prices[i+1] - prices[i]
        return maxx