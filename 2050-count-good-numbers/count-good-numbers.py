class Solution(object):
    def countGoodNumbers(self, n):
        even_positions = (n + 1)//2
        odd_positions = n // 2
        even = self.recurrsion(5,even_positions)
        odd = self.recurrsion(4,odd_positions)
        return (even * odd) % (10**9 + 7)
    def recurrsion(self,base,spec):
        mod = 10**9 + 7
        result = 1
        while spec > 0:
            if spec % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            spec //= 2
        return result