class Solution(object):
    def generate(self, numRows):
        sol = []
        for i in range(numRows):
            row = [1]
            ans = 1
            for j in range(1,i+1):
                ans = ans * (i + 1 - j) // j
                row.append(ans)
            sol.append(row)
        return sol