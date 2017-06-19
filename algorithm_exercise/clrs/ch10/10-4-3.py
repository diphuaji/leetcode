import tree
def printTree(node):
    s=[] 
    lastAct=None
    while True:
        if len(s)>0:
            lastAct=s.pop()
        if node.left==None and node.right==None:
            s.append(lastAct*-1)
            node=node.p
            continue
        if lastAct is  None or lastAct >0:
            print node.key
        if lastAct is not None and lastAct<0:
            if lastAct==-1:
                if node.right==None:
                    node=node.p
                    if len(s)==0:
                        break
                    s.append(s.pop()*-1)
                    continue
                s.append(2)
                node=node.right
                continue
            node=node.p
            if len(s)==0:
                break
            continue
        if node.left!=None:
            node=node.left
            s.append(1)
            continue
        node=node.right
        s.append(2)
t=tree.buildTree()
printTree(t.root)
