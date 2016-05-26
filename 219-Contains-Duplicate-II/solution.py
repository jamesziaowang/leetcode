class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        numsDic = dict();
        for y in range(len(nums)):
            x = numsDict.get(nums[y])
            if y and x-d <=k:
                return True
            else:
                numsDict[nums[y]] = y
        return False