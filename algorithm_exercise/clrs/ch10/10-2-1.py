class Element:
    def __init__(self,k=None):
        self.next=None     
        self.key=k
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,k):
        e =Element(k)
        if self.head is not None:
            e.next=self.head.next
            self.head.next=e
        else:
            self.head=e
        if self.tail is not None:
            self.tail=self.head
        
    def search(self,k):
        e=self.head
        while e is not None:            
            if e.key==k:
                return e.key
            e=e.next
        return e
    def delete(self,k):
        prev=None
        e=self.head
        while e is not None:
            if e.key==k:
                if prev is not None:
                    prev.next=e.next
                else:
                    self.head=e
                return
            prev=e
            e=e.next
l=LinkedList()
l.insert(5)
l.insert(8)
l.insert(120)
l.insert(21)
print l.search(2)
print l.search(21)
l.delete(8)
print l.search(8)
print l.search(5)
e=l.head
while e is not None:
    print "e: "+str(e.key)
    e=e.next
