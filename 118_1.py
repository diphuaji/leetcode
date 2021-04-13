class Solution(object):
    def compute_row(self, ans, rowIdx):
        if rowIdx == 0:
            row = [1]
            ans.append(row)
            return row
        last_row = self.compute_row(ans, rowIdx - 1)
        row = []
        for i in xrange(rowIdx+1):
            value = 0
            if i - 1 > -1:
                value += last_row[i-1]
            if i < rowIdx:
                value += last_row[i]
            row.append(value)
        ans.append(row)
        return row

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        self.compute_row(ans, numRows-1)
        return ans
