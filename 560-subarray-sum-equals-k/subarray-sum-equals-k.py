class Solution(object):
    def subarraySum(self, nums, k):
        count,summ = 0 , 0
        hashmap = {0:1}
        for i in nums:
            summ += i
            if (summ - k) in hashmap :
                count += hashmap[summ - k]
            hashmap[summ] = hashmap.get(summ,0) + 1
        return count 