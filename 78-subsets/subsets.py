class Solution(object):
    def subsets(self, nums):
        res = []
        n = len(nums)
        def recurrsion(i,temp):
            if i >= n:
                res.append(temp[:])
                return
            temp.append(nums[i])
            recurrsion(i+1,temp)
            temp.pop()
            recurrsion(i+1,temp)
        recurrsion(0,[])
        return res