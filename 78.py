'''
78. Subsets
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cache=[0 for i in nums]
        ans=[[]]
        if len(nums)==1:
            ans.append(nums)
            return ans
        self.solve(cache,0,0,ans,nums)
        return ans
    def solve(self,cache,index,pos,ans,nums):
        for i in xrange(pos,len(nums)):
            cache[index]=nums[i]
            ans.append(list(cache[:index+1]))
            if i!=len(nums)-1:
                self.solve(cache,index+1,i+1,ans,nums)
s=Solution()
print s.subsets([1,2,3,4])
