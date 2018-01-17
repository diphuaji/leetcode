class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums[abs(i)]<0:
                return abs(i)
            nums[abs(i)]*=-1