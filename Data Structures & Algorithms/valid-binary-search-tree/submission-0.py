# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Just checked the immediate neighbours and not the entire tree.
        def isBST(root: Optional[TreeNode], low: float, high: float):
            if not root:
                return True
            if not (low < root.val < high):
                return False
            return isBST(root.left, low, root.val) and isBST(root.right, root.val, high)
        return isBST(root, float('-inf'), float('inf'))
        