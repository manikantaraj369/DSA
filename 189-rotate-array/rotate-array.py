class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        if n == 0:
            return
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
    def reverse(self,nums,first,last):
        while first <= last:
            nums[first] , nums[last] = nums[last] , nums[first]
            first += 1
            last -= 1
