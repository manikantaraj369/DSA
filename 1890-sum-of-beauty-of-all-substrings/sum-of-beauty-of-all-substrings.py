class Solution(object):
    def beautySum(self, s):
        total_beauty = 0
        for i in range(len(s)):
            hash1 = {}
            for j in range(i,len(s)):
                hash1[s[j]] = hash1.get(s[j],0) + 1
                freq = hash1.values()
                max_freq = max(freq)
                min_freq = min(freq)
                total_beauty += (max_freq - min_freq )
        return total_beauty