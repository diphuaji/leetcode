class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """       
        n=len(matrix)        
        for i in xrange(n/2):            
            for j in xrange(n-i*2-1):
                rtCount=0
                r=i
                c=j+i
                tempR=None
                last=matrix[r][c]
                while rtCount<4:
                    temp=matrix[c][n-1-r]
                    matrix[c][n-1-r]=last
                    last=temp
                    tempR=r
                    r=c
                    c=n-1-tempR
                    rtCount+=1
s=Solution()
m=[[1,2,3],[4,5,6],[7,8,9]]
s.rotate(m)
print m

            
