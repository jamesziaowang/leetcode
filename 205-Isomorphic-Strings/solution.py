class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = dict()
        slen = len(s)
        tlen = len(t)
        if slen != tlen:
            return False
        for i in range(slen):
            tempS = sDict.get(s[i])
            if tempS and tempS != t[i]:
                return False
            tempS[s[i]] = t[i]
        return True
            
            