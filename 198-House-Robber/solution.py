class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            dp[i] = max(nums[i-1], nums[i-2]+nums[i])
        return dp