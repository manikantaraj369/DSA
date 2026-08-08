class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        if n == 0:
            return
        self.reverse(nums, 0, n - 1)

            # Step 2: reverse first k elements
        self.reverse(nums, 0, k - 1)

            # Step 3: reverse remaining n-k elements
        self.reverse(nums, k, n - 1)
    def reverse(self,nums,start,end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
