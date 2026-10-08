class Solution(object):
    def reverseString(self, s):
        n = len(s)
        low = 0
        high = n - 1
        while low < high:
            s[low] , s[high] = s[high], s[low]
            low += 1
            high -= 1
        return s