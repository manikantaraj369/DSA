class Solution(object):
    def reverse(self, x):
        sign = 0
        if x < 0:
            sign = -1
        else :
            sign = 1
        x = abs (x) 
        rev = 0
        while x > 0:
            last_digit = x % 10
            rev = rev * 10 + last_digit
            x = x//10
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return (rev * sign)
