#566. Reshape the Matrix 
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        oldR=len(nums)
        oldC=len(nums[0])
        if oldR*oldC!=r*c:
            return nums
        m=[[0 for x in xrange(c)] for j in xrange(r)]
        rCount=cCount=0
        for i in xrange(oldR):
            for l in xrange(oldC):                
                if cCount==c:
                    cCount=0
                    rCount+=1
                m[rCount][cCount]=nums[i][l]
                cCount+=1
        return m        
s=Solution()
print s.matrixReshape([[1,2],[3,4]],4,1)