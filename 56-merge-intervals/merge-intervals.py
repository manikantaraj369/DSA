class Solution(object):
    def merge(self, intervals):
        ans = []
        intervals.sort()
        for i in intervals:
            if not ans or ans[-1][1] < i[0]:
                ans.append(i)
            else :
                ans[-1][1] = max(ans[-1][1],i[1])
        return ans