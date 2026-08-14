class Solution(object):
    def longestConsecutive(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        st = set(nums)
        max_count = 1
        for j in st:
            if j - 1 not in st:
                count = 1
                x = j
                while x + 1 in st:
                    count += 1
                    x += 1
                max_count = max(max_count,count) 
        return max_count