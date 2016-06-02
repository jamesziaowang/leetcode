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
            while j<len(pre) && j<len(strs[i]):
                if pre[j] != strs[i][j]:
                    break;
                pre = pre[0:j]
        return pre