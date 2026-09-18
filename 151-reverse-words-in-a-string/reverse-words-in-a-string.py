class Solution(object):
    def reverseWords(self, s):
        res = []
        i = 0
        n = len(s)
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            j = i
            while j < n and s[j] != " ":
                j += 1
            if i < j:#for safty purpose
                res.append(s[i:j])
            i = j
        low = 0
        high = len(res) - 1
        while low < high:
            res[low] , res[high] = res[high] , res[low]
            low += 1
            high -= 1
        return " ".join(res)