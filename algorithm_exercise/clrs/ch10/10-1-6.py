from stack import MyStack
class NewQueue:
    def __init__(self,n=5):
        self._s1=MyStack(5)
        self._s2=MyStack(5)
    def enqueue(self,e):
        self._s2.push(e)
    def dequeue(self):        
        while not self._s2.empty():
            self._s1.push(self._s2.pop())
        e = self._s1.pop()
        while not self._s1.empty():
            self._s2.push(self._s1.pop())
        return e
    def empty(self):
        return self._s2.empty()
q=NewQueue()
q.enqueue(1)
q.enqueue(3)
print q.dequeue()
