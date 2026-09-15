class Solution(object):
    def maximum(self,mat,coloumn,n,m):
        maxi = float('-inf')
        index = -1
        for i in range(n):
            if mat[i][coloumn] > maxi:
                maxi = mat[i][coloumn]
                index = i
        return index
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high)//2
            row = self.maximum(mat,mid,n,m) 
            left = mat[row][mid - 1] if mid > 0 else -1
            right = mat[row][mid + 1] if (mid + 1) < m else -1
            if left < mat[row][mid] > right:
                return [row,mid]
            elif left > mat[row][mid]:
                high = mid - 1
            else:
                low = mid + 1
        return [-1,-1]