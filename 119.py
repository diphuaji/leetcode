'''
119. Pascal's Triangle II
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans=[1]
        if rowIndex==0: return ans
        ans.append(1)
        if rowIndex==1: return ans
        for i in xrange(2,rowIndex+1):
            j=k=0
            for m in xrange(i):
                k=ans[m]
                ans[m]+=j
                j=k
            ans.append(1)
        return ans