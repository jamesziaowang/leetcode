class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for x in range(len(matrix)):
            y = len(matrix[x])-1
            while y and matrix[x][y] > target:
                y-=1
            if matrix[x][y] == target:
                return True
        return False