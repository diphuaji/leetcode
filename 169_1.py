class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = {}
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num] = numDict[num]+1
            if numDict[num] > len(nums)//2:
                return num
