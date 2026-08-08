class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        if n == 0:
            return
        temp = nums[-k:]
        for i in range(n-k-1,-1,-1):
            nums[i+k] = nums[i]
        for i in range(k):
            nums[i] = temp[i]
        return nums