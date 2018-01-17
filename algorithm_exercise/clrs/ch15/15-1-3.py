def down_top(p,n,ans,c):
    ans[0]=0
    for i in xrange(1,n+1):
        maxP=0
        for j in xrange(1,i+1):
            maxP=max(maxP,p[j-1]+ans[i-j])
            if i-j!=0:
                maxP-=c
        ans[i]=maxP
    return ans[n]
if __name__=='__main__':
    p=[1,5,8,9,10,17,17,20,24,30]
    ans={}
    #print top_down(p,10,ans)
    print down_top(p,10,ans,5)
