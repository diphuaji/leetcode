import tree
def printTree(node):
    if node!=None:
        print "key:"+str(node.key)
        printTree(node.left)
        printTree(node.right)
t=tree.buildTree()
printTree(t.root)
