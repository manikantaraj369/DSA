class Solution(object):
    def getRow(self, rowIndex):
        res = [1] 
        row = 1
        for i in range(1,rowIndex+1):
            row = row * (rowIndex - i + 1)// i
            res.append(row)
        return res