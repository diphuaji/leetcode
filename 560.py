'''
560. Subarray Sum Equals K
'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==1:
            return int(nums[0]==k)
        c=0
        d={nums[0]:1}
        for i in xrange(1,len(nums)):
            nums[i]+=nums[i-1]
            if nums[i] in d:
                d[nums[i]]+=1
                continue
            d[nums[i]]=1
        for i in nums:
            d[i]-=1
            if (k+i) in d:
                c+=d[k+i]
            if i==k:
                c+=1
        return c