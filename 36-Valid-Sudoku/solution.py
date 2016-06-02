class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        strSet = set()
        for i in range(9):
            for j in range(9):
                if str[i][j]!='.' and str[i][j] in strSet:
                    return False
                elif str[i][j]!='.':
                    strSet.add(str[i][j])
            strSet.clear()
    
        strSet.clear()
        for i in range(9):
            for j in range(9):
                if str[j][i]!='.' and str[j][i] in strSet:
                    return False
                elif str[j][i]!='.':
                    strSet.add(str[j][i])
            strSet.clear()
    
        for i in range(0,9,3):
            for j in range(0,9,3):
                for k in range(9):
                    if str[i+int(k/3)][j+int(k%3)]!='.' and str[i+int(k/3)][j+int(k%3)] in strSet:
                        return False
                    elif str[i+int(k/3)][j+int(k%3)]!='.':
                        strSet.add(str[i+int(k/3)][j+int(k%3)])
                    strSet.clear()
        
        return True
            
        