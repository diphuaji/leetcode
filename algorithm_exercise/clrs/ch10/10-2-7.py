from linked_list import LinkedList

def reverse(l):
    nextTemp=l.head
    current=None
    temp=None
    while nextTemp !=None:
        temp=nextTemp
        nextTemp=nextTemp.next
        temp.next=current
        current=temp
    temp=l.head
    l.head=l.tail
    l.tail=temp

l=LinkedList()
l.insert(1)
l.insert(5)
l.insert(9)
l.insert(3)
e=l.head
while e!=None:
    print e.key
    e=e.next
reverse(l)
e=l.head
while e!=None:
    print e.key
    e=e.next
