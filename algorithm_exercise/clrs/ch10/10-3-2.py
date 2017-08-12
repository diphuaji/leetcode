KEY=0
PREV=1
NEXT=2
SIZE=3
FREE=None
def bulidList(n=5):
    global FREE,SIZE
    return [None for xrange(n*SIZE)]
def alloc(l):
    global KEY,PREV,NEXT,FREE
    temp=FREE
    FREE=l[FREE+NEXT]
    return temp
def free(pos,l):
    global KEY,PREV,NEXT,FREE
    l[pos+NEXT]=FREE
    FREE=pos
