class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        retStr = ""
        while n:
            retStr = chr((n-1)%26 + ord('A')) + retStr
            n = (n-1)/26
        return retStr
        