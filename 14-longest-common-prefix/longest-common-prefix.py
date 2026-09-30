class Solution(object):
    def longestCommonPrefix(self, s):
        n = len(s[0])
        if not s:
            return ""
        for i in range(n):
            char = s[0][i]
            for j in range(1,len(s)):
                if i == len(s[j]) or char != s[j][i]:
                    return s[0][:i]
        return s[0]