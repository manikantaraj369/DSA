class Solution(object):
    def search(self, nums, target):
        def binry(nums,low,high,target):
            if low > high:
                return -1
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binry(nums,low,mid-1,target)
            elif nums[mid] < target:
                return binry(nums,mid+1,high,target)
        return binry(nums,0,len(nums)-1,target)