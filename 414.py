'''
414. Third Maximum Number
'''
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        if len(nums)<3: return max(nums)
        count=0
        temp=0
        for i in xrange(len(nums)):
            if nums[i] is None:
                continue
            count+=1
            for j in xrange(i+1,len(nums)):
                if nums[j] is not None and nums[i]<nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
            for j in xrange(i+1,len(nums)):
                if nums[j]==nums[i]:
                    nums[j]=None
            if count==1:
                maxV=nums[i]
            if count==3:
                return nums[i]
            nums[i]=None
        return maxV