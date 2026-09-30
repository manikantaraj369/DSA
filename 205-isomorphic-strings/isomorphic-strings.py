class Solution(object):
    def isIsomorphic(self, s, t):
        hashst = {}
        hashts = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if (c1 in hashst and hashst[c1] != c2) or (c2 in hashts and hashts[c2] != c1):
                return False
            hashst[c1] = c2
            hashts[c2] = c1
        return True