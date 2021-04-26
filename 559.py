"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from Queue import Queue


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        current_count = 1
        next_count = 0
        max_depth = 0

        if root is not None:
            q = Queue()
            q.put(root)
            while not q.empty():
                node = q.get()
                next_count += len(node.children)
                current_count -= 1
                for child in node.children:
                    q.put(child)
                if current_count == 0:
                    current_count = next_count
                    next_count = 0
                    max_depth += 1

        return max_depth
