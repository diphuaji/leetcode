'''
121. Best Time to Buy and Sell Stock
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        prof=maxProf=0
        for i in xrange(1,len(prices)):
            prof+=prices[i]-prices[i-1]
            if prof<0:
                prof=0
                continue
            if prices[i]>prices[i-1]:
                maxProf=max(maxProf,prof)
        return maxProf