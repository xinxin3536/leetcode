class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        minn = prices[0]
        for i in range(0,len(prices)):
            if prices[i] < minn:
                minn = prices[i]
            if prices[i] - minn > maxx:
                maxx = prices[i] - minn
        return maxx