class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i,j = len(a)-1,len(b)-1
        c=0
        s=""
        while i>=0 or j>=0:
            if i>=0:
                c += int(a[i]) 
                i-=1
            else:
                c += 0
                
            if j>=0:
                c += int(a[j]) 
                j-=1
            else:
                c += 0
                
            s = str(c % 2) + s
            c /= 2
        return s
            