class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            req = target - nums[i]
            if req in nums:
                index = nums.index(req)
                if index != i:
                    return [i,index] 

