'''
64. Minimum Path Sum
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        maxNum=max(m,n)
        cache=[0 for i in xrange(maxNum)]
        curCache=[0 for i in xrange(maxNum)]
        lastStart=0        
        minV=0xffffffff
        for step in xrange(m+n-1):
            #print "step:"+str(step)
            start=max(step-n+1,0)            
            end=min(step,m-1)                       
            for r in xrange(start,end+1):                
                incre=0                
                c=step-r
                if r-1>=0:                        
                    incre=cache[r-1]
                    if c-1>=0:                        
                        incre=min(cache[r-1],
                        cache[r])
                elif c-1>=0:
                    incre=cache[r]
                #print start,r,c,cache,incre,maxNum
                minV=incre+grid[r][c]
                curCache[r]=minV
            cache=list(curCache)
        return minV        
s=Solution()
grid=[[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
#grid=[[1,2],[5,6],[1,1]]
#grid=[[1,3,1],[1,5,1],[4,2,1]]
print s.minPathSum(grid)
