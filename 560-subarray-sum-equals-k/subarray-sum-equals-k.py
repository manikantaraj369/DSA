class Solution(object):
    def subarraySum(self, nums, k):
        n = len(nums)
        count,summ = 0 , 0
        hashmap = {}
        hashmap[0] = 1
        for i in range(n):
            summ += nums[i]
            rem = summ - k
            if rem in hashmap :
                count += hashmap[rem]
            hashmap[summ] = hashmap.get(summ,0) + 1
        return count 