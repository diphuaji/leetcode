import tree
def printTree(node):
    if node is None:
        return
    print node.key
    printTree(node.left)
    printTree(node.sib)
    return
t=tree.buildRootedTree()
printTree(t.root)
