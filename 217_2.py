class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numDict = {}
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
                continue
            return True
        return False
