class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(len(nums)):
            x^=i
            x^=nums[i]
        return x ^ len(nums)
