class Solution(object):
    def removeOuterParentheses(self, s):
        res = []
        dept = 0
        for i in s:
            if i == "(":
                if dept > 0:
                    res.append(i)
                dept += 1
            else:
                dept -= 1
                if dept > 0:
                    res.append(i)        
        return "".join(res)