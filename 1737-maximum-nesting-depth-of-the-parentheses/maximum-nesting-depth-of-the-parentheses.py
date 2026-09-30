class Solution(object):
    def maxDepth(self, s):
        count = 0
        max_count = 0
        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                max_count = max(count,max_count)
                count -= 1
        return max_count