def solve(nums):
    for i in xrange(len(nums)):
        j=i
        temp=0
        while j >0:
            if nums[j-1]>nums[j]:
                temp=nums[j-1]
                nums[j-1]=nums[j]
                nums[j]=temp
            j-=1
    return nums    
print solve([2,3,1,2,3,6,8,5,7,9,34])
