class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(len(n)):
            x^=i
            x^=n[i]
        return x ^ len(n)
