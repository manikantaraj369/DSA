class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high)//2
            totalhours = 0
            for i in piles:
                totalhours += (i // mid + (1 if i % mid != 0 else 0))
            if totalhours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        