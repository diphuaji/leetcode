'''
611. Valid Triangle Number
time limited exceeded
'''
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in xrange(len(nums)):
            if i==len(nums)-1 or nums[i]==0:
                continue
            for j in xrange(i+1,len(nums)):
                if j==len(nums)-1 or nums[j]==0:
                    continue
                for k in xrange(j+1,len(nums)):
                    if nums[k]==0:
                        continue
                    if (nums[i]+nums[j])>nums[k] and abs(nums[i]-nums[j])<nums[k]:
                        c+=1
        return c
                    
        