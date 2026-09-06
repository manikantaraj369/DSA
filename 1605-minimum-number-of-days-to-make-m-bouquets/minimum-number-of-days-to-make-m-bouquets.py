class Solution(object):
    def is_count (slef,bloomDay,day,m,k):
        count = 0
        bouque = 0
        for i in bloomDay:
            if i <= day:
                count += 1
                if count == k:
                    bouque += 1
                    count = 0
            else:
                count = 0
        return bouque >= m 
    def minDays(self, bloomDay, m, k):
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if self.is_count(bloomDay,mid,m,k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans