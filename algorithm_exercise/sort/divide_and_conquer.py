def merge(nums,p,q,r):
    left=[]
    right=[]
    #print p,q,r
    for i in xrange(q-p):
        left.append(nums[p+i])
    for i in xrange(r-q):
        right.append(nums[q+i])
    left.append(0xffffffff)
    right.append(0xffffffff)
    j=k=0
    for i in xrange(p,r):
        if left[j]<right[k]:
            nums[i]=left[j]
            j+=1
            continue
        nums[i]=right[k]
        k+=1
def solve(nums,p,q,r):
    if r-p>1:        
        solve(nums,p,(q+p)//2,q)
        solve(nums,q,(r+q)//2,r)
        merge(nums,p,q,r)

nums=[2,5,3,6,2,1,1,3,3,9,4,2,2,5,6]
solve(nums,0,len(nums)//2,len(nums))
print nums

