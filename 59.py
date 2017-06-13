'''
59. Spiral Matrix II
'''
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[[0 for i in xrange(n)] for j in xrange(n)]
        maxDepth=n//2+n%2
        depth=0
        head=1
        while depth<maxDepth:            
            if n%2 and depth==maxDepth-1:
                ans[depth][depth]=head
                break            
            nowCount=n-2*depth
            rCount=cCount=0
            left=down=True
            while not ((not down) and (rCount==0) and (left)):                
                ans[rCount+depth][cCount+depth]=head
                head+=1
                if left and down:
                    cCount+=1
                    if cCount==nowCount-1:
                        left=False
                    continue
                if not left and down:
                    rCount+=1
                    if rCount==nowCount-1:
                        down=False
                    continue
                if not left and not down:                    
                    cCount-=1
                    if cCount==0:                        
                        left=True
                    continue
                rCount-=1                
            depth+=1
        return ans
s=Solution()
print s.generateMatrix(6)
