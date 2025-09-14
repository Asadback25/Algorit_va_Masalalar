#Binary trees
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(6)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

# Recursive Pre Order Traversal (DFS) Time: O(N), Space: O(N)
def pre_order(node):
    if not node:
        return

    print(node.val)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)
