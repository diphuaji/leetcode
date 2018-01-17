from queue import MyQueue
class NewStack:
    def __init__(self,n=5):
        self._q1=MyQueue(n)
        self._q2=MyQueue(n)
    def push(self,e):
        while not self._q1.empty():
            self._q2.enqueue(self._q1.dequeue())
        self._q1.enqueue(e)
        while not self._q2.empty():
            self._q1.enqueue(self._q2.dequeue())
    def pop(self):
        return self._q1.dequeue()

stack=NewStack(5)
stack.push(3)
stack.push(5)
print stack.pop()
print stack.pop()
print stack.pop()
