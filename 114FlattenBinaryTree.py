# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        self.prev = None
        def flattenTree(node):
            if not node:
                return
            flattenTree(node.right)
            flattenTree(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node
        flattenTree(root)
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
