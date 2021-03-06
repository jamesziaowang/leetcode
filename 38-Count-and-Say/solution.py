class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        oldstr = "1"
        for i in range(n-1):
            count=1
            curStr = ""
            for j in range(1,len(oldstr)+1):
                if j<len(oldstr) and oldstr[j]==oldstr[j-1]:
                    count+=1
                else:
                    curStr = curStr + str(count)+oldstr[j-1]
                    count = 1
            oldstr = curStr
        return oldstr