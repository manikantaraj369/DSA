class Solution(object):
    def combinationSum(self, nums, target):
        n = len(nums)
        res = []
        def recurrsion(index,target,temp):
            if index == n:
                if target == 0:
                    res.append(temp[:])
                return
            if nums[index] <= target:
                temp.append(nums[index])
                recurrsion(index,target - nums[index],temp)
                temp.pop()
            recurrsion(index + 1, target , temp)
        recurrsion(0,target,[])
        return res