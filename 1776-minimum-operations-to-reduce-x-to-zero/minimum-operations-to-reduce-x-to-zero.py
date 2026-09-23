class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        max_index = -1
        current_sum = 0
        left = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum > target and left <=right:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_index = max(max_index,right - left + 1)
        return len(nums) - max_index if max_index != -1 else -1