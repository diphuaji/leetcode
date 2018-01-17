def solve(nums):
    ans=[]
    if len(nums)<2:
        return nums
    for i in xrange(len(nums)):
        index=0
        minV=nums[index]
        for j in xrange(1,len(nums)):
            if minV>nums[j]:
                index=j
                minV=nums[j]
        ans.append(nums[index])
        del nums[index]
    return ans
print solve([5,1,2,3,3,5,8,4,6,78])
            
