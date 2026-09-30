class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        hash1 = {} 
        for i in range(len(s)):
            hash1[s[i]] = hash1.get(s[i],0) + 1
        for i in range(len(t)):
            if t[i] not in hash1 or hash1[t[i]] == 0:
                return False
            hash1[t[i]] -= 1
        return True