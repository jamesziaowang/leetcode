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
            for j in range(len(strs[i])):
                if j>len(pre) or pre[j] != strs[i][j]:
                    pre = pre[0:j]
                    break;
        return pre