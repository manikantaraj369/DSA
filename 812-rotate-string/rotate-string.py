class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if goal == s[i:] + s[:i]:
                return True
        return False
        # return goal in (s + s)