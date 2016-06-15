class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums): return 0
        nums = sorted(nums, reverse=True)
        return nums[k-1]