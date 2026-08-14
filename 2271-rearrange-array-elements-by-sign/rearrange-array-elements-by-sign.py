class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        neg = []
        pos = []
        for i in range(n):
            if nums[i] < 0:
                neg.append(nums[i])
            else :
                pos.append(nums[i])
        for i in range(n//2):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        return nums

