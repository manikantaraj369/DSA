class Solution(object):
    def isPalindrome(self, x):
        rev = 0
        temp = x
        while x > 0:
            last_digit = x % 10
            rev = rev * 10 + last_digit
            x = x // 10
        return temp == rev


        