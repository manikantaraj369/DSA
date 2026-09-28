from collections import Counter
class Solution(object):
    def frequencySort(self, s):
    #     freq = Counter(s)
    #     def logic(char):
    #         return (-freq[char],char)
    #     array = sorted(freq.keys(),key = logic)
    #     return "".join(char * freq[char] for char in array)
        ans = []
        for i in set(s):
            c = s.count(i)
            ans.append((c,i))
        ans.sort(reverse = True)
        res = ""
        for i,c in ans:
            res += c*i
        return res
        