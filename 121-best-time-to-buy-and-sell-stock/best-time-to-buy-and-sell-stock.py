class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        mini = prices[0]
        maxxprofit = 0
        cost = 0
        for i in range(n):
            cost = prices[i] - mini
            maxxprofit = max(maxxprofit,cost)
            mini  = min(mini,prices[i])
        return maxxprofit
