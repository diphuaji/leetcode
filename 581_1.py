#581. Shortest Unsorted Continuous Subarray 
class Solution(object):
    def findUnsortedSubarray(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end=start=-1
        small=nums[-1]
        big=nums[0]
        for i in xrange(len(nums)):
            if nums[i]>=big:big=nums[i]
            else: end=i
            if nums[-1-i]<=small:small=nums[-1-i]
            else: start=len(nums)-i-1
        if end==start: return 0
        print start,end
        return end-start+1
s=Solution()
print s.findUnsortedSubarray([2,1,3,4,4,4,9,2,5])
