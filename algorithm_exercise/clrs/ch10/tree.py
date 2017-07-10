class BTree:
    def __init__(self):
        self.root=None
class Node:
    def __init__(self,key):
        self.left=self.right=self.p=None
        self.key=key
data=[[1,12,7,3],
    [2,15,8,None],
    [3,4,10,None],
    [4,10,5,9],
    [5,2,None,None],
    [6,18,1,4],
    [7,7,None,None],
    [8,14,6,2],
    [9,21,None,None],
    [10,5,None,None]]
def buildTree():
    global data
    tree =BTree()
    nodeDic={}
    for item in data:
        node=None
        if item[0] in nodeDic:
            node=nodeDic[item[0]]
        else:
            node=nodeDic[item[0]]=Node(item[1])
        if item[0]==6:
            node.p=None
            tree.root=node
        if item[2]!=None:
            if item[2] in nodeDic:
                node.left=nodeDic[item[2]]
            else:
                nodeDic[item[2]]=node.left=Node(data[item[2]-1][1])
            node.left.p=node
        if item[3]!=None:
            if item[3] in nodeDic:
                node.right=nodeDic[item[3]]
            else:
                node.right=nodeDic[item[3]]=Node(data[item[3]-1][1])
            node.right.p=node
    return tree
if __name__=='__main__':
    tree = buildTree()
    print tree.root.p
    print tree.root.left
    print tree.root.right
