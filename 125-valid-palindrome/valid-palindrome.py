class Solution(object):
    def isPalindrome(self, s):
        cleaned_s = [char.lower() for char in s if char.isalnum()]
        def palindrome(i,n):
            if i >= len(cleaned_s)//2:
                return True
            if cleaned_s[i] !=  cleaned_s[n-i]:
                return False
            return palindrome(i + 1,n )
        return palindrome(0,len(cleaned_s) - 1)