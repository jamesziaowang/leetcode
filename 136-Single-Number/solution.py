class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for i range(len(nums)):
            num ^= nums(i)
        return num