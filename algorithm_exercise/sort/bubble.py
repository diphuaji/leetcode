def solve(nums):
    if len(nums)<2:
        return nums
    temp=0
    for i in xrange(len(nums)-1):
        for j in xrange(len(nums)-1,i-1,-1):
            if nums[j] <nums[j-1]:
                temp=nums[j]
                nums[j]=nums[j-1]
                nums[j-1]=temp
    return nums

print solve([1,6,3,2,2,2,9,3,6,1])
