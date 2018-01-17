'''
64. Minimum Path Sum
'''
class Solution(object):
    def __init__(self):
        self.minV=0xFFFFFFFF
        self.count=0
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r=c=sumV=0
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        self.solve(grid,r,c,m,n,sumV)
        return self.minV
    def solve(self,grid,r,c,m,n,sumV):
        sumV+=grid[r][c]
        if r==m-1 and c==n-1:
            self.minV=min(self.minV,sumV)
            self.count+=1
            print self.count
            return
        if r!=m-1:
            self.solve(grid,r+1,c,m,n,sumV)
        if c!=n-1:
            self.solve(grid,r,c+1,m,n,sumV)
s=Solution()
grid=[[1,3,4],[2,3,1],[6,5,4]]
s.minPathSum(grid)
