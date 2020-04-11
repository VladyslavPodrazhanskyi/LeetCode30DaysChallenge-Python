"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def diameter_of_binary_tree(root: Node) -> int:
    if not root:
        return 0  # edge case

    def fn(node):
        """Return length+1 and diameter rooted at node"""
        if not node:
            return 0, 0
        l1, d1 = fn(node.left)
        l2, d2 = fn(node.right)
        return 1 + max(l1, l2), max(d1, d2, l1 + l2)

    return fn(root)[1]
