'''
118. Pascal's Triangle
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        if numRows==0:
            return ans
        ans.append([1])
        if numRows==1:
            return ans
        ans.append([1,1])
        if numRows==2:
            return ans
        for i in xrange(2,numRows):
            row=[1]
            for j in xrange(i-1):
                row.append(ans[i-1][j]+ans[i-1][j+1])
            row.append(1)
            ans.append(row)
        return ans
