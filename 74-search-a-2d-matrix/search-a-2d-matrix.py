class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = (n*m) - 1 
        while low <= high:
            mid = (low + high)//2
            row = mid // m
            coloumn = mid % m
            if matrix[row][coloumn] == target:
                return True
            elif matrix[row][coloumn] < target:
                low = mid + 1
            else:
                high = mid -1
        return False