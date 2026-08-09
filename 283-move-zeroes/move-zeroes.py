class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        a = 0
        for i in range(n):
            if nums[i] != 0:
                nums[a] , nums[i] = nums[i] , nums[a]
                a += 1
        return nums