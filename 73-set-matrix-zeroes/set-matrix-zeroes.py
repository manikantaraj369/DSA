class Solution(object):
    def setZeroes(self, matrix):
        colom0 = 1
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else :
                        colom0 = 0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[0][i] = 0 
        if colom0 == 0:
            for j in range(n):
                matrix[j][0] = 0
        return matrix