class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        pre = strs[0]
        for i in range(1,len(strs)):
            j=0
            while j<len(pre) and j<len(strs[i]):
                if pre[j] != strs[i][j]:
                    break;
                j+=1
            pre = pre[0:j] if j>0 else ''
        return pre