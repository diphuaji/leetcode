'''
268. Missing Number 
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[x+1 for x in nums]
        for i in nums:
            if i!=len(nums)=1
                nums[abs(i)]*=-1
        for i in len(nums):
            if nums[i]>0:
                return i-1
        return len(nums)+1