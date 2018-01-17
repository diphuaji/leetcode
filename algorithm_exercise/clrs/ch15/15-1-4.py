def top_down(p,n,ans,sol):
    if n==0:
        return 0
    if n not in ans:
        ans[n]=0
        for i in xrange(1,n+1):
            curt=p[i-1]+top_down(p,n-i,ans,sol)
            if curt >ans[n]:
                ans[n]=curt
                sol[n]=i
    return ans[n]
def top_down_solve(p,n):
    ans={}
    sol={}
    top_down(p,n,ans,sol)
    result=[]
    val=ans[n]
    while n>0:
        result.append(sol[n])
        n-=sol[n]
        print n
    return val,result
if __name__=='__main__':
    p=[1,5,8,9,10,17,17,20,24,30]
    print top_down_solve(p,10)
