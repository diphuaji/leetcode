def top_down(p,n,ans):
    maxP=0
    if n==0:
        return 0
    if n not in ans:
        for i in xrange(1,n+1):
            maxP=max(maxP,p[i-1]+top_down(p,n-i,ans))
        ans[n]=maxP
    return ans[n]
def down_top(p,n,ans):
    ans[0]=0
    for i in xrange(1,n+1):
        maxP=0
        for j in xrange(1,i+1):
            maxP=max(maxP,p[j-1]+ans[i-j])
        ans[i]=maxP
    return ans[n]
if __name__=='__main__':
    p=[1,5,8,9,10,17,17,20,24,30]
    ans={}
    #print top_down(p,10,ans)
    print down_top(p,10,ans)
