class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        row = 0
        coloumn = m - 1
        while row < n and coloumn >= 0:
            if matrix[row][coloumn] == target:
                return True
            elif matrix[row][coloumn] < target:
                row += 1
            else:
                coloumn -= 1
        return False