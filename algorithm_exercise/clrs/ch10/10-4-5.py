import tree
def printTree(node):
    root=node
    down=True
    lastNode=None
    while True:
        if down:
            print node.key
            if node.left!=None:
                node=node.left
                continue
            if node.right!=None:
                node=node.right
                continue
            down=False
            lastNode=node
            node=node.p
            continue
        if lastNode==node.left:
            if node.right==None:
                if node==root:
                    break
                lastNode=node
                node=node.p
                continue
            node=node.right
            down=True
            continue
        if node==root:
            break
        lastNode=node
        node=node.p        
t=tree.buildTree()
printTree(t.root)
