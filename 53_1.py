class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.solve(nums,0,(len(nums)-1)//2,len(nums)-1)

    def maxMidSum(self,nums,p,mid,q):
        left=right=0
        leftSum=rightSum=-0xffffffff
        for i in xrange(mid,p-1,-1):
            left+=nums[i]
            leftSum=max(leftSum,left)
        for i in xrange(mid+1,q+1):
            right+=nums[i]
            rightSum=max(rightSum,right)
        return rightSum+leftSum
    def solve(self,nums,p,mid,q):
        if q==p:
            return nums[mid]
        left=self.solve(nums,p,(p+mid)//2,mid)
        right=self.solve(nums,mid+1,(mid+1+q)//2,q)
        midVal=self.maxMidSum(nums,p,mid,q)
        return max(left,right,midVal)
s=Solution()
print s.maxSubArray([-2,1])
