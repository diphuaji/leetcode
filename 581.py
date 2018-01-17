#581. Shortest Unsorted Continuous Subarray 
class Solution(object):
    def findUnsortedSubarray(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=end=-1
        dup=sorted(nums)
        for i in xrange(len(nums)):
            if nums[i]!=dup[i]:
                if start==-1: start=i
                end=i
        if end==start: return 0
        return end-start+1
s=Solution()
