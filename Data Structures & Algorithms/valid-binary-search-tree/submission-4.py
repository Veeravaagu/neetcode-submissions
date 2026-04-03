# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBST(root, float("-inf"), float("+inf"))
    def isBST(self, root, leftval, rightval):
        if not root:
            return True
        if not (leftval < root.val < rightval):
            return False
        return self.isBST(root.left, leftval, root.val ) and self.isBST(root.right, root.val, rightval)
    
        