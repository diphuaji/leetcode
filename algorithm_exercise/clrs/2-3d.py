p_count=0
def merge(nums,p,q,r):
    global p_count
    left=[]
    right=[]
    left=[nums[i] for i in xrange(p,q+1)]
    right=[nums[i] for i in xrange(q+1,r+1)]
    left.append(0xffffffff)
    right.append(0xffffffff)
    j=k=0
    for i in xrange(r-p+1):
        if left[j]>right[k]:
            nums[p+i]=right[k]
            k+=1
            p_count+=1
            continue
        nums[p+i]=left[j]
        j+=1
def sort_merge(nums,p,q,r):
    if r-p>0:
        sort_merge(nums,p,(q+p)/2,q)
        sort_merge(nums,q+1,(r+q)/2,r)
        merge(nums,p,q,r)
nums=[2,3,8,6,1]        
sort_merge(nums,0,len(nums)-1,len(nums)-1)
print nums,p_count
        
