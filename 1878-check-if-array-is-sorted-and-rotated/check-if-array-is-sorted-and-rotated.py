class Solution(object):
    def check(self, nums):
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i - 1] > nums[i]:
                count += 1
        return count <= 1
            