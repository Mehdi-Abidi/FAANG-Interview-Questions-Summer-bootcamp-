# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is None or root1 is None and root2 is not None:
            return False
        if root1.val!=root2.val:return False
        return (
            self.flipEquiv(root1.left,root2.left) and 
            self.flipEquiv(root1.right,root2.right)
            or
            self.flipEquiv(root1.left,root2.right) and 
            self.flipEquiv(root1.right,root2.left)
            )
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        
