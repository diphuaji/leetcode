class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=[]
        for x in nums:
            nums[abs(x)-1]*=-1
            if(nums[abs(x)-1])>0:
                r.append(abs(x))
        return r
s=Solution()
print s.findDuplicates([4,3,2,7,8,2,3,1])