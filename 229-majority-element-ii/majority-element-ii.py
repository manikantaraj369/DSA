class Solution(object):
    def majorityElement(self, nums):
        elm1,elm2 = None,None
        count1 ,count2 = 0 , 0
        for i in nums:
            if count1 == 0 and i != elm2:
                elm1 ,count1= i,1
            elif count2 == 0 and i != elm1:
                elm2 ,count2= i,1
            elif elm1 == i:
                count1 += 1
            elif elm2 == i:
                count2 += 1
            else :
                count1 -= 1
                count2 -= 1
        lis = []
        if nums.count(elm1) > (len(nums)//3):
            lis.append(elm1)
        if nums.count(elm2) > (len(nums)//3):
            lis.append(elm2)
        return lis