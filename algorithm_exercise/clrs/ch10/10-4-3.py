import tree
def printTree(node):
    s=[] 
    lastAct=None
    while True:
        if lastAct is None or lastAct >0:
            print node.key
        if node.left==None and node.right==None:
            s.append(s.pop()*-1)
            node=node.p
            continue
        if len(s)>0:
            lastAct=s.pop()
        if lastAct is not None and lastAct<0:
            if lastAct==-1:
                if node.right==None:
                    node=node.p
                    s.append(-2)
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
