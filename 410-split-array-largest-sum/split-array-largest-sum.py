class Solution(object):
    def counting(self,nums,min_pages,k):
        subarray = 1
        count = 0
        for i in range(len(nums)):
            if count + nums[i] > min_pages:
                subarray += 1
                count = nums[i]
            else:
                count += nums[i]
        return subarray <= k
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high)//2
            if self.counting(nums,mid,k):
                high = mid - 1
            else:
                low = mid + 1
        return low