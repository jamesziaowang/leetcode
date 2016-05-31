class Solution(object):
    def reverseNums(self, nums, start, end):
        for i in range(start, (start+end)/2):
            nums[i] ^= nums[end-i-1] 
            nums[end-i-1] ^= nums[i] 
            nums[i] ^= nums[end-i-1] 
        
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        self.reverseNums(nums, 0, n-k)
        self.reverseNums(nums, n-k, n)
        self.reverseNums(nums, 0, n-1)