class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        sumVal=0
        for i in xrange(len(nums)/2):
            sumVal+=nums[i*2]
        return sumVal
s=Solution()
print s.arrayPairSum([1,4,3,2])
