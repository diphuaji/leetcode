class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy_p = prices[0]
        for p in prices:
            if p < buy_p:
                buy_p = p
            else:
                tmp = p-buy_p
                if(profit < tmp):
                    profit = tmp
        return profit
