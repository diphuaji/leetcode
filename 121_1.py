class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        for i in xrange(len(prices)-1):
            prices[i]=prices[i+1]-prices[i]
        prices.pop()
        #print prices
        return self.solve(prices,0,(len(prices)-1)/2,len(prices)-1)
    def crossMid(self,prices,p,mid,q):
        maxL=maxR=l=r=0
        for i in xrange(mid,p-1,-1):
            l+=prices[i]
            maxL=max(maxL,l)
        for i in xrange(mid+1,q+1):
            r+=prices[i]
            maxR=max(maxR,r)
        #print maxL+maxR
        return maxL+maxR

    def solve(self,prices,p,mid,q):
        if q-p<1:
            return prices[mid]
        left=self.solve(prices,p,(mid+p)/2,mid)
        right=self.solve(prices,mid+1,(q+mid+1)/2,q)
        crossMid=self.crossMid(prices,p,mid,q)
        return max(left,right,crossMid)

s=Solution()
print s.maxProfit([3,5,9,1,22,3,21])
