'''
122. Best Time to Buy and Sell Stock II
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prof=0
        size=len(prices)
        if  size<2: 
            return 0
        l=h=prices[0]
        for i in xrange(1,size):
            if prices[i]>h:
                h=prices[i]
                if i=size-1:
                    prof+=h-l
                continue
            if h>l:
                prof+=h-l
            l=h=prices[i]
        return prof
