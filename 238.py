'''
238. Product of Array Except Self 
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=list(nums)
        length=len(nums)
        for i in xrange(1,length-1):
            nums[i]*=nums[i-1]
            res[length-i-1]*=res[length-i]
        for i in xrange(1,length-1):
            if i==length-1: 
                res[i]=nums[i-1]
                continue
            if i==0:
                res[i]=res[i+1]
                continue
            k[i]=k[i+1]*nums[i-1]
        return res
        