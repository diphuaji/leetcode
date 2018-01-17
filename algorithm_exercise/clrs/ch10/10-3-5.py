import string
lHead=lPrev=lNex=lKey=fHead=fPrev=fNex=fKey=lSize=None
def init(n):
    global lHead,lPrev,lNex,lKey,fHead,fPrev,fNex,fKey,lSize
    lSize=0    
    lPrev= [ None for x in xrange(n)]
    lNex=[ None for x in xrange(n)]
    lKey=[ None for x in xrange(n)]
    lHead=None
    fPrev= [ None for x in xrange(n)]
    fNex=[ None for x in xrange(n)]
    fKey=[ None for x in xrange(n)]    
    fHead=0
    for i in xrange(n):
        if i !=n-1:
            fNex[i]=i+1
        if i !=0:
            fPrev[i]=i-1
        fKey[i]=None
    return []

def printLink(isL=True):
    global lHead,lPrev,lNex,lKey,fHead,fPrev,fNex,fKey    
    if isL:
        head,prev,nex,key=lHead,lPrev,lNex,lKey
    else:
        head,prev,nex,key=fHead,fPrev,fNex,fKey
    index=head
    items=[]
    while index!=None:
        if isL:
            items.append('(%s:%s)' % (str(index),str(lKey[index])))
        else:
            items.append( str(index))
        index=nex[index]
    print '(isL:%s): %s' % (isL,string.join(items,'->'))

def insert(key):
    global lKey
    index=alloc()
    lKey[index]=key

def search(key):
    global lHead,lPrev,lNex,lKey
    index=lHead
    while index!=None and lKey[index]!=key:
        index=lNex[index]
    return index
    
def delete(key):
    index=search(key)
    if index!=None:
        free_obj(index)
    
def alloc():
    global lHead,lPrev,lNex,lKey,fHead,fPrev,fNex,fKey,lSize
    if fHead==None:
        raise Exception('out of space')    
    '''process L'''
    if lHead!=None:
        lPrev[lHead]=fHead
    lNex[fHead]=lHead
    lHead=fHead    
    '''process F'''
    temp=fHead
    fHead=fNex[fHead]
    fPrev[fHead]=None
    lSize+=1
    return temp

def free_obj(pos):
    global lHead,lPrev,lNex,lKey,fHead,fPrev,fNex,fKey,lSize
    '''process F'''
    if fHead!=None:
        fPrev[fHead]=pos
    fNex[pos]=fHead
    fHead=pos    
    '''process L'''
    if pos==lHead:
        lHead=lNex[lHead]    
    if lPrev[pos]!=None:
        lNex[lPrev[pos]]=lNex[pos]
    if lNex[pos]!=None:
        lPrev[lNex[pos]]=lPrev[pos]
    lSize-=1
    
def compactify():
    global lHead,lPrev,lNex,lKey,fHead,fPrev,fNex,fKey,lSize
    lIndex=lHead
    fIndex=fHead
    while lIndex!=None:
        if lIndex<lSize-1:
            lIndex=lNex[lIndex]
            continue
        while fIndex!=None and fIndex<lSize-1:
            fIndex=fNex[fIndex]
        if lIndex==None:
            raise Exception('F overflow!')
        '''process L'''
        lKey[fIndex]=lKey[lIndex]
        if lIndex==lHead:
            lHead=fIndex
        if lPrev[lIndex]!=None:
            lNex[lPrev[lIndex]]=fIndex
        if lNex[lIndex]!=None:
            lPrev[lNex[lIndex]]=fIndex
        '''process F'''
        if fIndex==fHead:
            fHead=lIndex
        if fPrev[fIndex]!=None:
            fNex[fPrev[fIndex]]=lIndex
        if fNex[fIndex]!=None:
            fPrev[fNex[fIndex]]=lIndex        
        fIndex=fNex[fIndex]
        lIndex=lNex[lIndex]
        
            
if __name__=='__main__':    
    init(5)
    print '--alloc--'
    insert('h')
    printLink(True)
    printLink(False)
    print 'lSize: %s, FullSize: %s' % (str(lSize),str(5))
    
    print '--alloc--'
    insert('d')
    printLink(True)
    printLink(False)
    print 'lSize: %s, FullSize: %s' % (str(lSize),str(5))
    
    print '--alloc--'
    insert('p')
    printLink(True)
    printLink(False)
    print 'lSize: %s, FullSize: %s' % (str(lSize),str(5))
    
    print '--free-- 0'
    delete('d')
    printLink(True)
    printLink(False)
    print 'lSize: %s, FullSize: %s' % (str(lSize),str(5))
    
    print '--compactify--'
    compactify()
    printLink(True)
    printLink(False)
    print 'lSize: %s, FullSize: %s' % (str(lSize),str(5))
