class MyStack:
   # def __init__(self):
   #     self._array=[0 for i in 10]
   #     self._pos=0
    def __init__(self,n=10):
        self._array=range(n)
        self._pos=0
    def empty(self):
        return self._pos==0
    def push(self,e):
        if self._pos==len(self._array)-1:
            raise Exception('stack overflow')
        self._array[self._pos]=e
        self._pos+=1
        return e
    def pop(self):
        if self._pos==0:
            raise Exception('stack underflow')
        self._pos-=1
        return self._array[self._pos]
s=MyStack()
for i in xrange(5):
    s.push(2)
for i in xrange(5):
    print s.pop()
