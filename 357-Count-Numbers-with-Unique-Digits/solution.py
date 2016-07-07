class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        n = min(n, 10)
        dp = [1]+[9]*n
        for i in range(2,n+1):
            for x in range(9,9-i+1,-1):
                dp[i] *=x
        return sum(dp)
        