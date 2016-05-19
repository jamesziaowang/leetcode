class Solution(object):
    def maxProfit(self, prices):
        res = 0
        low = sys.maxint
        n = len(prices)
        for i in range(1, n):
            low = min(low, prices[i-1])
            res = max(res, prices[i] - low)
        return res    
    