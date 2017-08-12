allocNum=0
free = 0 
prev = []
nex = []
val = []
head = None
def init(n):
    global free,prev,nex,val,allocNum,head
    prev= [ None for x in xrange(n)]
    nex=[ None for x in xrange(n)]
    val=[ None for x in xrange(n)]
    head=None
    free =0
    for i in xrange(n):
        nex[i]=prev[i]=val[i]=None
        if i !=n-1:
            nex[i]=i+1
def alloc():
    global head,free,prev,nex,val,allocNum
    if free==None:
        raise Exception('out of space')
    temp=free
    free =nex[free]    
    nex[temp]=head
    prev[temp]=None
    if head!=None:
        prev[head]=temp
    head=temp 
    allocNum+=1
    return temp
def free_obj(pos):
    global free,prev,nex,val,allocNum,head
    if allocNum!=0 and pos<=allocNum-1:
        if prev[pos]!=None:
            nex[prev[pos]]=nex[pos]
        if nex[pos]!=None:
            prev[nex[pos]]=prev[pos]
        '''
        usually if pos=head, we set head=next[pos]
        '''
        if pos==head:
            head=nex[pos]
        if pos!=allocNum-1:            
            if prev[allocNum-1]!=None:
                nex[prev[allocNum-1]]=pos
            if nex[allocNum-1]!=None:
                prev[nex[allocNum-1]]=pos            
            val[pos]=val[allocNum-1]
            nex[pos]= nex[allocNum-1]
            prev[pos]=prev[allocNum-1]
        '''
        but if the new head is moved to pos(which means next[pos]=allocNum-1), we have to to further set head=pos
        '''
        if head==allocNum-1:
            head=pos
        lastFree=free
        free = allocNum-1
        nex[free]=lastFree
        allocNum-=1
init(5)
print "--aloc--"
alloc()
print "--aloc--"
alloc()
print "--aloc--"
alloc()
print "free:%s" % free
print "prev:%s" % str(prev)
print "next:%s" % str(nex)
print "head:%s" % head
print "--free-- 1"
free_obj(1)
print "free:%s" % free
print "prev:%s" % str(prev)
print "next:%s" % str(nex)
print "head:%s" % head
alloc()
print "--aloc--"
print "free:%s" % free
print "prev:%s" % str(prev)
print "next:%s" % str(nex)
print "head:%s" % head

print "--free-- 0"
free_obj(0)
print "free:%s" % free
print "prev:%s" % str(prev)
print "next:%s" % str(nex)
print "head:%s" % head
free_obj(0)
print "--free-- 0"
print "free:%s" % free
print "prev:%s" % str(prev)
print "next:%s" % str(nex)
print "head:%s" % head

