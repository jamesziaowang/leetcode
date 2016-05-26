class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = dict()
        tDict = dict()
        for i in range(len(s)):
            tStr, sStr  = sDict.get(t[i]), tDict.get(s[i])
            if tStr is None and sStr is None:
                sDict[t[i]] ,tDict[s[i]] = s[i],t[i]
            elif tStr != s[i] and sStr != t[i]:
                return False
        return True