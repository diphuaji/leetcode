class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]]
        if numRows > 1:
            ans.append([1, 1])
        if numRows < 3:
            return ans
        for i in xrange(2, numRows):
            row = [1]
            for j in xrange(1, i):
                row.append(ans[i-1][j-1]+ans[i-1][j])
            row.append(1)
            ans.append(row)
        return ans
