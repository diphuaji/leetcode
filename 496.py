#496. Next Greater Element I 
class Solution(object):
    def nextGreaterElement(self, findNums, nums):    
        ans=[]
        for num in findNums:
            i = nums.index(num)
            while i <len(nums):
                if num < nums[i]:
                    ans.append(nums[i])
                    break
                i+=1
            if i==len(nums): ans.append(-1)
        return ans
s = Solution()
print repr(s.nextGreaterElement([4,1,2],[1,3,4,2]))
