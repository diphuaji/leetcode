def top_down(n,ans):
    if n in ans:
        return ans[n]
    ans[n]=top_down(n-2,ans)+top_down(n-1,ans)
    return ans[n]
def down_top(n):
    ans={1:1,2:1}
    if n not in ans:
        for i in xrange(3,n+1):
            ans[i]=ans[i-2]+ans[i-1]
    return ans[n]
if __name__=='__main__':
    #print down_top(6)
    ans={1:1,2:1}
    print top_down(6,ans)

