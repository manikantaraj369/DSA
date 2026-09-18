class Solution(object):
    def largestOddNumber(self, num):
        # first = 0
        # last = 0
        # n = len(num)
        # for i in range(n-1,-1,-1):
        #     if int(num[i]) % 2 != 0:
        #         last = i + 1
        #         break
        # for j in range(n):
        #     if num[i] == '0':
        #         first = i + 1
        #     else:
        #         break
        # return num[first:last]
        return num.rstrip('02468')