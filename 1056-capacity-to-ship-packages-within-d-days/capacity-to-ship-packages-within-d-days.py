class Solution(object):
    def counting(self,weights,elm,limit):
        days = 1
        count = 0
        for i in weights:
            if (count + i) > elm:
                days += 1
                count = i
            else:
                count += i
        return days <= limit 
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if self.counting(weights,mid,days):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans