class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        numsDict = dict();
        for y in range(len(nums)):
            x = numsDict.get(nums[y])
            if y and y-x <=k:
                return True
            else:
                numsDict[nums[y]] = y
        return False