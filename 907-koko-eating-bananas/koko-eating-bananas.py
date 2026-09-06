class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high)//2
            if self.counting(piles,mid) <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    def counting(self,piles,hourly):
        totalhours = 0
        for i in piles:
            totalhours += (i // hourly + (1 if i % hourly != 0 else 0))
        return totalhours