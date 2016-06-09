class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i,j = len(a),len(b)
        while i>=0 and j>=0:
            c += int(a[i-=1]) if i>=0 else 0
            c += int(a[j-=1]) if j>=0 else 0
            s = str(c % 2) + s
            c /= 2
        return s
            