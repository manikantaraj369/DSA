class Solution(object):
    def counting(self,nums,elem,limit):
        totalcount = 0
        for i in nums:
            totalcount += (i + elem - 1) // elem
        return totalcount <= limit
    def smallestDivisor(self, nums, threshold):
        low = 1
        high = max(nums)
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if self.counting(nums,mid,threshold):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans