class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        p1 = p2 = 0
        ret =[]
        while p1 < len(nums1) and p2< len(nums2):
            if nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p1 += 1
                p2 += 1
                ret.append(nums1[p1])
        return ret