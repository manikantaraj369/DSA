class Solution(object):
    def majorityElement(self, nums):
        elm1,elm2 = 0,0
        count1 ,count2 = 0 , 0
        n = len(nums)
        for i in range(n):
            if count1 == 0 and nums[i] != elm2:
                count1 = 1
                elm1 = nums[i]
            elif count2 == 0 and nums[i] != elm1:
                count2 = 1
                elm2 = nums[i]
            elif elm1 == nums[i]:
                count1 += 1
            elif elm2 == nums[i]:
                count2 += 1
            else :
                count1 -= 1
                count2 -= 1
        count1 , count2 = 0,0
        for i in range(n):
            if nums[i] == elm1:
                count1 += 1
            elif nums[i] == elm2:
                count2 += 1
        lis = []
        if count1 > (n//3):
            lis.append(elm1)
        if count2 > (n//3):
            lis.append(elm2)
        return lis